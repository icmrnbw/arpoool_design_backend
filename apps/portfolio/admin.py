from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.portfolio.models import Service, Project, Inquiry, SiteSettings, Client


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    pass


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteSettings)
class SocialAdmin(admin.ModelAdmin):
    pass
