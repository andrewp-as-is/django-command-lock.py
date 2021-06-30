from django.contrib import admin

from .models import Command

class CommandAdmin(admin.ModelAdmin):
    list_display = ['id','app','name','is_locked',]
    list_filter = ('app', 'is_locked',)
    search_fields = ('app', 'name',)

admin.site.register(Command, CommandAdmin)
