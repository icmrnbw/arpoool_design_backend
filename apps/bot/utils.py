import asyncio
import json
from datetime import timedelta
from typing import Optional

import telegram
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.utils.translation import gettext as _
from telegram.constants import ParseMode

from apps.bot.models import TelegramAccount


def get_user(update: telegram.Update) -> tuple[Optional[TelegramAccount], bool]:
    """
        Returns existing TelegramUser instance if exists, creates a new one otherwise.
        Updates information about user in the database if it was previously updated more than day ago
    :param update:
    :return:
    """
    # Get telegram user
    if update.effective_user is None:
        return None, False

    queryset = TelegramAccount.objects.filter(id=update.effective_user.id)
    if queryset.exists():
        user = queryset.get()

        # Update user data if time has come
        if user.last_update_date + timedelta(days=1) < timezone.localtime():
            user.first_name = update.effective_user.first_name
            user.last_name = update.effective_user.last_name
            user.username = update.effective_user.username
            user.last_update_date = timezone.now()
            user.save()

        created = False
    else:
        user = TelegramAccount.objects.create(id=update.effective_user.id, first_name=update.effective_user.first_name,
                                              last_name=update.effective_user.last_name,
                                              username=update.effective_user.username)
        created = True

    return user, created


def parse_update(request_token: str, request) -> telegram.Update:
    async def coroutine():
        # Parse telegram update from json
        async with telegram.Bot(settings.BOT_TOKEN) as bot:
            update = telegram.Update.de_json(json.loads(request.body), bot)

        return update

    # Abort request if it is not from telegram
    if settings.BOT_TOKEN != request_token:
        raise PermissionDenied('Token checking failed')

    return asyncio.run(
        coroutine()
    )


def send_message_to_admins(message: str):
    async def coroutine():
        admins = TelegramAccount.objects.filter(is_admin=True)
        sent_count = 0

        async with telegram.Bot(settings.BOT_TOKEN) as bot:
            async for obj in admins:
                await bot.send_message(chat_id=obj.id, text=message, parse_mode=ParseMode.HTML)
                sent_count += 1

        return sent_count

    return asyncio.run(
        coroutine()
    )


def send_hello(user: TelegramAccount):
    async def coroutine():
        async with telegram.Bot(settings.BOT_TOKEN) as bot:
            await bot.send_message(chat_id=user.id, text=_('Hello!'))

    asyncio.run(
        coroutine()
    )
