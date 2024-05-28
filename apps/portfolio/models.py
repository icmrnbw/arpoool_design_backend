from django.db import models
from django.utils.translation import gettext_lazy as _

from .base_model import BaseModel


class Service(BaseModel):
    name = models.CharField(verbose_name=_('Название'), max_length=255)
    tools = models.CharField(verbose_name=_('Инструмент'), max_length=255)
    tag = models.CharField(verbose_name=_('Тэг'), max_length=255)
    description = models.TextField(verbose_name=_('Описание'), )
    tools_description = models.TextField(verbose_name=_('Описание инструментов'), )
    picture = models.ImageField(verbose_name=_('Картинка'), )
    active = models.BooleanField(verbose_name=_('Активна'), default=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Project(BaseModel):
    name = models.CharField(verbose_name=_('Название'), max_length=255)
    service = models.ManyToManyField(verbose_name=_('Услуга'), to=Service)
    description = models.TextField(verbose_name=_('Описание'), )
    year = models.CharField(verbose_name=_('Год'), max_length=9)  # чтобы могло поместиться 2023-2024, как в фигме
    client = models.CharField(verbose_name=_('Клиент'), max_length=255)
    preview = models.ImageField(verbose_name=_('Превью'), )
    content_picture = models.ImageField(verbose_name=_('Контентное изображение'), )
    active = models.BooleanField(verbose_name=_('Активен'), default=True)
    show_at_main = models.BooleanField(verbose_name=_('Показывать на главной странице'), default=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class Client(BaseModel):
    name = models.CharField(verbose_name=_('Название'), max_length=255)
    picture = models.ImageField(verbose_name=_('Картинка'), )
    active = models.BooleanField(verbose_name=_('Активен'), default=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    name = models.CharField(verbose_name=_('Имя'), max_length=255)
    phone = models.CharField(verbose_name=_('Номер телефона'), max_length=15)
    comment = models.TextField(verbose_name=_('Сообщение'), blank=True, null=True)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return self.name
