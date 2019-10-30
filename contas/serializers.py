from rest_framework import serializers

from contas.models import CentroLucro, CentroCusto, ContaReceber, ContaPagar


class CentroLucroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroLucro
        fields = '__all__'


class CentroCustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCusto
        fields = '__all__'


class ContaReceberSerializer(serializers.ModelSerializer):
    atrasado = serializers.ReadOnlyField()

    class Meta:
        model = ContaReceber
        fields = [
            'id',
            'centro_lucro',
            'descricao',
            'valor',
            'previsao_recebimento',
            'observacao',
            'recebido',
            'data_recebimento',
            'data_cadastro',
            'atrasado',
        ]
        depth = 1


class ContaPagarSerializer(serializers.ModelSerializer):
    atrasado = serializers.ReadOnlyField()

    class Meta:
        model = ContaPagar
        fields = [
            'id',
            'centro_custo',
            'descricao',
            'valor',
            'data_vencimento',
            'pago',
            'data_pagamento',
            'observacao',
            'data_cadastro',
            'atrasado',
        ]
        depth = 1

