import telegram
from django.db import models
from django.utils.translation import gettext as _


class TelegramAccount(models.Model):
    id = models.BigIntegerField(verbose_name='ID', primary_key=True, unique=True)  # Equal to telegram ID of user
    is_admin = models.BooleanField(_('Является админом'), help_text=_('Только администраторы будут получать уведомления'),
                                   default=False)

    joined_date = models.DateTimeField(_('Дата подключения'), auto_now_add=True)
    last_update_date = models.DateTimeField(_('Дата последнего изменения'), auto_now_add=True, editable=True)

    username = models.CharField(_('Юзернейм'), null=True, blank=True, max_length=32)
    first_name = models.CharField(_('Имя'), max_length=64)
    last_name = models.CharField(_('Фамилия'), null=True, blank=True, max_length=64)

    has_blocked_the_bot = models.BooleanField(_('Заблокировал бота'), default=False)

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
        verbose_name = _('Пользователь Telegram')
        verbose_name_plural = _('Пользователи Telegram')
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['is_admin']),
        ]
