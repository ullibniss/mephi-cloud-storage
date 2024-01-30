from django.contrib import admin

from .models import *

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    fields = ('title', 'description')
    save_on_top = True



admin.site.register(Document, FileAdmin)

admin.site.site_title = 'Админ-панель облачного хранилища'
admin.site.site_header = 'Админ-панель облачного хранилища'