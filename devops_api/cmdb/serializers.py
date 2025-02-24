from cmdb.models import Idc, ServerGroup, Server
from rest_framework import serializers


class IdcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idc
        fields = "__all__"
        read_only_fields = ('id',)


class ServerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerGroup
        fields = "__all__"
        read_only_fields = ('id',)


class ServerSerializer(serializers.ModelSerializer):
    # idc = IdcSerializer(read_only=True)
    # server_group = ServerGroupSerializer(many=True, read_only=True)

    class Meta:
        model = Server
        fields = "__all__"
        read_only_fields = ('id',)
