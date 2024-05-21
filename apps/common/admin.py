from django.contrib import admin

from .logsender.models import LogSenderBot, BackupDbBot


@admin.register(LogSenderBot)
class LogSenderBotAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "token", "bot_username", "channel_name", "channel_id", "created_at", "updated_at",)


@admin.register(BackupDbBot)
class BackupDbBotAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "token", "bot_username", "channel_name", "channel_id", "created_at", "updated_at",)
