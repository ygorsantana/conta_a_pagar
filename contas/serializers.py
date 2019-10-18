from rest_framework import serializers

from contas.models import CentroLucro


class CentroLucroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroLucro
        fields = '__all__'
