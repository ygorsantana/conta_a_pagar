from django.shortcuts import render
from rest_framework import viewsets

from contas.filters import CentroLucroFilter, CentroCustoFilter, ContaReceberFilter, ContaPagarFilter
from contas.models import CentroLucro, CentroCusto, ContaReceber, ContaPagar
from contas.serializers import CentroLucroSerializer, CentroCustoSerializer, ContaReceberSerializer, \
    ContaPagarSerializer
from django_filters import rest_framework as rest_filters
from rest_framework import filters


class CentroLucroViewset(viewsets.ModelViewSet):
    queryset = CentroLucro.objects.all().exclude(excluido=True).order_by('descricao')
    serializer_class = CentroLucroSerializer
    filter_backends = (rest_filters.DjangoFilterBackend,)
    filterset_class = CentroLucroFilter


class CentroCustoViewset(viewsets.ModelViewSet):
    queryset = CentroCusto.objects.all().exclude(excluido=True).order_by('descricao')
    serializer_class = CentroCustoSerializer
    filter_backends = (rest_filters.DjangoFilterBackend,)
    filterset_class = CentroCustoFilter


class ContaReceberViewset(viewsets.ModelViewSet):
    queryset = ContaReceber.objects.all().order_by('previsao_recebimento')
    serializer_class = ContaReceberSerializer
    filter_backends = (rest_filters.DjangoFilterBackend,)
    filterset_class = ContaReceberFilter


class ContaPagarViewset(viewsets.ModelViewSet):
    queryset = ContaPagar.objects.all().order_by('data_vencimento')
    serializer_class = ContaPagarSerializer
    filter_backends = (rest_filters.DjangoFilterBackend,)
    filterset_class = ContaPagarFilter
