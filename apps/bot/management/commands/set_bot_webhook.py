import asyncio

import telegram
from django.conf import settings
from django.core.management import BaseCommand, CommandError
from django.urls import reverse


async def _set_webhook(uri):
    async with telegram.Bot(settings.BOT_TOKEN) as bot:
        result = await bot.set_webhook(uri, allowed_updates=[])

    return result


class Command(BaseCommand):
    help = 'Set Telegram Bot webhook'

    def add_arguments(self, parser):
        parser.add_argument('domain', nargs=1, type=str)

    def handle(self, *args, **options):
        url: str = options['domain'].pop()

        if url.startswith('http') or '://' in url:
            raise CommandError('Argument "domain" must not include scheme')
        if '/' in url:
            raise CommandError('Argument "domain" must not contain any forward slashes. It should be like "example.com"')

        uri = f'https://{url}' + reverse('bot:webhook', args=[settings.BOT_TOKEN])
        result = asyncio.run(_set_webhook(uri))

        if result:
            uri = uri[:-30] + '*' * 30
            self.stdout.write(f'Telegram Bot: WebHook successfully set to {uri} (some characters were hidden)')
        else:
            raise CommandError('Could not set webhook')
