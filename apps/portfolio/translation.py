from modeltranslation.translator import register, TranslationOptions
from .models import Service, Project


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'tools_description',)


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
