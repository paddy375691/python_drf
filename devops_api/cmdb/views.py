from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView
from django.conf import settings

import json
import os

from cmdb.serializers import IdcSerializer, ServerGroupSerializer, ServerSerializer
from cmdb.models import Idc, ServerGroup, Server
from libs.ssh import SSH
from system_config.models import Credential


class IdcViewSet(ModelViewSet):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['city']
    search_fields = ['name']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            res = {'code': 200, 'msg': "创建成功"}
        else:
            res = {'code': 500, 'msg': "创建失败"}
        return Response(res)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            res = {'code': 200, 'msg': "更新成功"}
        else:
            res = {'code': 500, 'msg': "更新失败"}
        return Response(res)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
            res = {'code': 200, 'msg': "删除成功"}
        except Exception as e:
            res = {'code': 500, 'msg': '该IDC机房关联其他主机，请先删除关联的主机再操作！'}
        return Response(res)


class ServerGroupViewSet(ModelViewSet):
    queryset = ServerGroup.objects.all()
    serializer_class = ServerGroupSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class ServerViewSet(ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'hostname', 'public_ip', 'private_ip']
    search_fields = ['idc', 'server_group']


class HostCollectView(APIView):
    def get(self, request):
        hostname = request.query_params.get('hostname')
        server = Server.objects.get(hostname=hostname)
        ssh_ip = server.ssh_ip
        ssh_port = server.ssh_port

        credential_id = request.query_params.get('credential_id')
        # 选择凭据
        if credential_id:
            credential_id = int(credential_id)
        # elif not credential_id and not server.credential:
        #     res = {'code': 500, 'msg': '未发现凭据，请选择！'}
        #     return Response(res)
        elif server.credential:
            credential_id = server.credential.id

        # 通过凭据ID获取SSH用户名和密码
        credential = Credential.objects.get(id=credential_id)
        username = credential.username
        if credential.auth_mode == 1:
            password = credential.password
            ssh = SSH(ssh_ip, ssh_port, username, password=password)
        else:
            private_key = credential.private_key  # key的内容，并不是一个文件
            ssh = SSH(ssh_ip, ssh_port, username, key=private_key)

        # 测试是否SSH连接成功
        result = ssh.test()
        if result['code'] == 200:
            client_agent_name = "host_collect.py"
            local_file = os.path.join(settings.BASE_DIR, 'cmdb', 'files', client_agent_name)
            remote_file = os.path.join(settings.CLIENT_COLLECT_DIR, client_agent_name)
            tmpresult = ssh.scp(local_file, remote_file)
            print(tmpresult)
            result = ssh.command('python %s' % remote_file)
            if result['code'] == 200:
                data = json.loads(result['data'])
                data['is_verified'] = 'verified'
                data['credential'] = credential_id
                Server.objects.filter(hostname=hostname).update(**data)
                res = {'code': 200, 'msg': '主机配置同步成功！'}
            else:
                res = {'code': 500, 'msg': '主机配置同步失败！错误：%s' % result['msg']}
        else:
            res = {'code': 500, 'msg': '%s' % result['msg']}
        return Response(res)
