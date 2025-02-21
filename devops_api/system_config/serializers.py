from system_config.models import Credential
from rest_framework import serializers


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = "__all__"
        read_only_fields = ('id',)
