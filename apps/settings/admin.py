from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.settings.models import SiteSetting


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    class MyModelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # manually set the current instance on the widget
            self.fields['data'].widget.instance = self.instance

    list_display = ('description', 'key')
    form = MyModelForm

    fieldsets = [
        (None, {'fields': ['description', 'key', 'data']}),
        (_('Технические данные'), {'fields': ['schema'], 'classes': ['collapse']})
    ]
    readonly_fields = ('description', 'key', 'schema')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
