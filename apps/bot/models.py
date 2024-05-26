import telegram
from django.db import models
from django.utils.translation import gettext as _


class TelegramAccount(models.Model):
    id = models.BigIntegerField(verbose_name='ID', primary_key=True, unique=True)  # Equal to telegram ID of user
    is_admin = models.BooleanField(_('Is admin'), help_text=_('Only administrators will receive notifications'),
                                   default=False)

    joined_date = models.DateTimeField(_('Joined date'), auto_now_add=True)
    last_update_date = models.DateTimeField(_('Last update date'), auto_now_add=True, editable=True)

    username = models.CharField(_('Username'), null=True, blank=True, max_length=32)
    first_name = models.CharField(_('First name'), max_length=64)
    last_name = models.CharField(_('Last name'), null=True, blank=True, max_length=64)

    has_blocked_the_bot = models.BooleanField(_('Blocked the bot'), default=False)

    def __str__(self):
        name = self.full_name()
        return f'@{self.username} - {name}' if self.username else name

    def __repr__(self):
        return f'<TelegramUser id: {self.id}, first_name: "{self.first_name}", last_name: "{self.last_name}"'

    @property
    def priority(self) -> int:
        return int(self.is_admin)

    def full_name(self):
        return ' '.join(item for item in (self.first_name, self.last_name) if item is not None)

    class Meta:
        verbose_name = _('Telegram User')
        verbose_name_plural = _('Telegram Users')
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['is_admin']),
        ]
