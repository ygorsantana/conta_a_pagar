import django_filters

from contas.models import CentroLucro


class CentroLucroFilter(django_filters.FilterSet):
    descricao = django_filters.CharFilter(field_name='descricao', lookup_expr='icontains')

    class Meta:
        model = CentroLucro
        fields = ('descricao',)

