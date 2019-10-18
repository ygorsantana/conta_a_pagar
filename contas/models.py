import uuid

from colorfield.fields import ColorField
from django.db import models


# Create your models here.
class CentroCusto(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
    )
    descricao = models.CharField(
        max_length=200,
        null=False,
    )
    cor = models.CharField(
        max_length=7,
        null=False,
    )
    previsao_custo = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
    )
    excluido = models.BooleanField(
        default=0,
        null=False,
    )


class CentroLucro(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
    )
    descricao = models.CharField(
        max_length=200,
        null=False,
    )
    cor = ColorField(
        null=False,
    )
    excluido = models.BooleanField(
        default=0,
        null=False,
    )


class CentroCustoPrevisao(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
    )
    centro_custo = models.ForeignKey(
        CentroCusto,
        null=False,
        on_delete=models.CASCADE,
    )
    ano = models.IntegerField(
        null=False
    )
    mes = models.IntegerField(
        null=False
    )
    previsao_custo = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
    )


class ContaPagar(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
    )
    centro_custo = models.ForeignKey(
        CentroCusto,
        null=False,
        on_delete=models.CASCADE,
    )
    descricao = models.CharField(
        max_length=200,
        null=True,
    )
    parcela_atual = models.IntegerField(
        null=False,
    )
    quantidade_parcelas = models.IntegerField(
        null=False,
    )
    valor_parcela = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
    )
    valor_total = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
    )
    data_vencimento = models.DateTimeField(
        null=True,
    )
    pago = models.BooleanField(
        null=False,
    )
    data_pagamento = models.DateTimeField(
        null=True,
    )
    observacao = models.TextField(
        null=True,
    )
    data_cadastro = models.DateTimeField(
        null=False,
    )
    ordem = models.IntegerField(
        null=False,
    )


class ContaPagarAnexo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
    )
    conta_pagar = models.ForeignKey(
        ContaPagar,
        null=False,
        on_delete=models.CASCADE,
    )
    nnome_arquivo = models.CharField(
        max_length=200,
        null=True,
    )
    observacao = models.TextField(
        null=True,
    )
    data_envio = models.DateTimeField(
        null=False,
    )


class ContaReceber(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
    )
    descricao = models.CharField(
        max_length=200,
        null=True,
    )
    parcela_atual = models.IntegerField(
        null=False,
    )
    valor_parcela = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
    )
    previsao_recebimento = models.DateTimeField(
        null=True,
    )
    observacao = models.TextField(
        null=True,
    )
    recebido = models.BooleanField(
        null=True,
    )
    data_recebimento = models.DateTimeField(
        null=True,
    )
    data_cadastro = models.DateTimeField(
        null=False,
    )
    ordem = models.IntegerField(
        null=False,
    )


class ContaReceberAnexo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
    )
    conta_receber = models.ForeignKey(
        ContaReceber,
        null=False,
        on_delete=models.CASCADE,
    )
    nome_arquivo = models.CharField(
        max_length=200,
        null=False,
    )
    observacao = models.TextField(
        null=True,
    )
    data_envio = models.DateTimeField(
        null=False,
    )
