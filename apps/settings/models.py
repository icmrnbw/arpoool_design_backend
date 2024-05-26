from django.db import models
from django.utils.translation import gettext as _
from django_jsonform.models.fields import JSONField

from apps.settings.translation_utils import expand_schema_translation


class SiteSetting(models.Model):
    key = models.CharField(_('Ключ'), max_length=16, unique=True)
    description = models.CharField(_('Описание'), max_length=250)
    data = JSONField(_('Данные'), schema=lambda x: expand_schema_translation(x.schema))
    schema = models.JSONField(_('Схема'))

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]
        verbose_name = _('Настройки сайта')
        verbose_name_plural = _('Настройки сайта')

    def __str__(self):
        return self.description

    def __repr__(self):
        return (f'<{self.__class__.__name__}(key={self.key}, description={self.description}, '
                f'data={self.data}, schema={self.schema})>')
