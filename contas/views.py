from django.shortcuts import render
from rest_framework import viewsets

from contas.filters import CentroLucroFilter
from contas.models import CentroLucro
from contas.serializers import CentroLucroSerializer
from django_filters import rest_framework as filters



class CentroLucroViewset(viewsets.ModelViewSet):
    queryset = CentroLucro.objects.all()
    serializer_class = CentroLucroSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CentroLucroFilter
# pq ta vindo os paramketros como 0 1 2 3
#