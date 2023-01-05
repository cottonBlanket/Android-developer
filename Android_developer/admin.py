from django.contrib import admin

# Register your models here.
from .models import *


class TextAdminInline(admin.StackedInline):
    model = Text
    extra = 1


class ImageAdminInline(admin.StackedInline):
    model = Image
    extra = 1


class TableAdminInline(admin.StackedInline):
    model = Table
    extra = 1


class PageAdmin(admin.ModelAdmin):
    inlines = (TextAdminInline, ImageAdminInline, TableAdminInline)


admin.site.register(Page, PageAdmin)
admin.site.register(Text)
admin.site.register(Image)
admin.site.register(Table)


