from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from system_config.models import Credential
from system_config.serializers import CredentialSerializer


class CredentialViewSet(ModelViewSet):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

    def create(self, request, *args, **kwargs):
        serilaizer = self.get_serializer(data=request.data)
        if serilaizer.is_valid():
            self.perform_create(serilaizer)
            res = {'code': 200, 'msg': '创建成功'}
        else:
            res = {'code': 500, 'msg': '创建失败'}
        return Response(res)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            res = {'code': 200, 'msg': '更新成功'}
        else:
            res = {'code': 500, 'msg': '更新失败'}
        return Response(res)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
            res = {'code': 200, 'msg': '删除成功'}
        except Exception as e:
            res = {'code': 500, 'msg': '该凭据关联了主机，请先删除关联的主机'}
        return Response(res)
