import django_filters

from contas.models import CentroLucro, CentroCusto


class CentroLucroFilter(django_filters.FilterSet):
    descricao = django_filters.CharFilter(field_name='descricao', lookup_expr='icontains')

    class Meta:
        model = CentroLucro
        fields = ('descricao',)


class CentroCustoFilter(django_filters.FilterSet):
    descricao = django_filters.CharFilter(field_name='descricao', lookup_expr='icontains')

    class Meta:
        model = CentroCusto
        fields = ('descricao',)
