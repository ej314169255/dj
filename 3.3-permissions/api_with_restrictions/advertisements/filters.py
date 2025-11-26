import django_filters

from advertisements.models import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = django_filters.DateFromToRangeFilter(field_name='created_at')
    status = django_filters.CharFilter(lookup_expr='icontains')
    creator = django_filters.CharFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']
