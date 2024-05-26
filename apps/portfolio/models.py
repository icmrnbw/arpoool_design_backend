from django.db import models
from django_jsonform.models.fields import JSONField

from .base_model import BaseModel


class Service(BaseModel):
    name = models.CharField(max_length=255)
    tools = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    description = models.TextField()
    tools_description = models.TextField()
    picture = models.ImageField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name


class Project(BaseModel):
    name = models.CharField(max_length=255)
    service = models.ManyToManyField(Service)
    description = models.TextField()
    year = models.CharField(max_length=9)  # чтобы могло поместиться 2023-2024, как в фигме
    client = models.CharField(max_length=255)
    preview = models.ImageField()
    content_picture = models.ImageField()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class Client(BaseModel):
    name = models.CharField(max_length=255)
    picture = models.ImageField()

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return self.name
