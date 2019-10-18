from django.shortcuts import render
from rest_framework import viewsets

from contas.models import CentroLucro
from contas.serializers import CentroLucroSerializer


class CentroLucroViewset(viewsets.ModelViewSet):
    queryset = CentroLucro.objects.all()
    serializer_class = CentroLucroSerializer
