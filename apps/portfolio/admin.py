from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.portfolio.models import Service, Project, Inquiry, Client


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'tools', 'tag', 'active',)
    search_fields = ('name', 'tools', 'tag')
    list_filter = ('tag',)
    list_editable = ('active',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_services', 'year', 'client', 'active', 'show_at_main')
    search_fields = ('name', 'description', 'year', 'client')
    list_filter = ('year', 'client', 'service')
    autocomplete_fields = ('service',)
    list_editable = ('active', 'show_at_main')

    @admin.display(description=_('Услуга'))
    def get_services(self, obj):
        return ", ".join([service.name for service in obj.service.all()])


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)
    search_fields = ('name',)
    list_filter = ('name',)
    list_editable = ('active',)


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'comment')
    search_fields = ('name', 'phone')
    list_filter = ('name',)
