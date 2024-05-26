from django.urls import path

from apps.bot.views import TelegramView

app_name = 'bot'

urlpatterns = [
    path('bot/<token>/', TelegramView.as_view(), name='webhook'),
]
