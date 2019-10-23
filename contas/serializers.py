from rest_framework import serializers

from contas.models import CentroLucro, CentroCusto


class CentroLucroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroLucro
        fields = '__all__'


class CentroCustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCusto
        fields = '__all__'
