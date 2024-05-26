## Notifications bot
A Django application for sending notifications in Telegram

**Setting things up:**
1) Install `python-telegram-bot` using `python -m pip install python-telegram-bot`
2) Add application to `INSTALLED_APPS` in your `settings.py`
3) Set `BOT_TOKEN` in your `settings.py`
4) Add bot urls into your root urlconfig as follows:
    ```python
    urlpatterns = [
        path('', include('apps.bot.urls', namespace='bot'))
    ]
    ```
5) Run migrations `python manage.py migrate`
6) Set webhook using management command `python manage.py set_bot_webhook yourdomain.com`
7) Done.

**Usage:**
The application defines model `TelegramAccount` and registers admin interface for it. 
Every Telegram user that has started the bot will appear in the table. You can send 
notification to all admins using utility function `send_message_to_admins("Hello")`, 
which is defined in `bot.utils`. The notification message will be sent only to users
that has column "Is admin" checked in admin panel.
