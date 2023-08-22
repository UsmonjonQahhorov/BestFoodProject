from django.contrib import admin

from users.models import User, TgUser

admin.site.register(User)
admin.site.register(TgUser)