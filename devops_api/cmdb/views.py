from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from cmdb.serializers import IdcSerializer, ServerGroupSerializer, ServerSerializer
from cmdb.models import Idc, ServerGroup, Server


class IdcViewSet(ModelViewSet):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

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


class ServerViewSet(ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
