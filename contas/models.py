import datetime
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


class ContaPagar(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    centro_custo = models.ForeignKey(
        CentroCusto,
        null=False,
        on_delete=models.CASCADE,
    )
    descricao = models.CharField(
        max_length=200,
        null=False,
    )
    valor = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=False,
    )
    data_vencimento = models.DateTimeField(
        null=True,
    )
    pago = models.BooleanField(
        null=True,
    )
    data_pagamento = models.DateTimeField(
        null=True,
    )
    observacao = models.TextField(
        null=True,
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
    )

    @property
    def atrasado(self):
        if self.data_pagamento and self.data_pagamento > self.data_vencimento:
            return True
        if datetime.datetime.now() > self.data_vencimento.replace(tzinfo=None):
            return True
        return False


class ContaReceber(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
    )
    centro_lucro = models.ForeignKey(
        CentroLucro,
        null=False,
        on_delete=models.CASCADE,
    )
    descricao = models.CharField(
        max_length=200,
        null=False,
    )
    valor = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=False,
    )
    previsao_recebimento = models.DateTimeField(
        null=False,
    )
    observacao = models.TextField(
        null=True,
    )
    recebido = models.BooleanField(
        default=False,
    )
    data_recebimento = models.DateTimeField(
        null=True,
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
    )

    @property
    def atrasado(self):
        if self.data_recebimento and self.data_recebimento > self.previsao_recebimento:
            return True
        if datetime.datetime.now() > self.previsao_recebimento.replace(tzinfo=None):
            return True
        return False
