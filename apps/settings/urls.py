from django.urls import path
from . import jsonform_views

urlpatterns = [
    path('jsonform-file-handler/', jsonform_views.file_handler_view),
]
