from django.contrib import admin

from apps.bot.models import TelegramAccount


@admin.register(TelegramAccount)
class TelegramAccountAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'is_admin', 'has_blocked_the_bot')
    search_fields = ('first_name', 'last_name', 'username')
    readonly_fields = ('full_name', 'has_blocked_the_bot', 'id', 'joined_date', 'last_update_date',
                       'username', 'first_name', 'last_name')
    list_editable = ('is_admin',)
    list_filter = ('is_admin', 'has_blocked_the_bot')
