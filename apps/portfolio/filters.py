import django_filters
from .models import Project, Service


class ProjectFilter(django_filters.FilterSet):
    service = django_filters.ModelMultipleChoiceFilter(
        queryset=Service.objects.all(),
    )

    class Meta:
        model = Project
        fields = ['service']
