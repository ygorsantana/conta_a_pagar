from django.shortcuts import render
from rest_framework import viewsets

from contas.filters import CentroLucroFilter, CentroCustoFilter
from contas.models import CentroLucro, CentroCusto
from contas.serializers import CentroLucroSerializer, CentroCustoSerializer
from django_filters import rest_framework as filters


class CentroLucroViewset(viewsets.ModelViewSet):
    queryset = CentroLucro.objects.all()
    serializer_class = CentroLucroSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CentroLucroFilter


class CentroCustoViewset(viewsets.ModelViewSet):
    queryset = CentroCusto.objects.all()
    serializer_class = CentroCustoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CentroCustoFilter
