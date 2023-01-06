from django.contrib import admin
from .models import *


class ContentAdminInline(admin.StackedInline):
    model = Content
    extra = 1


class PageAdmin(admin.ModelAdmin):
    inlines = (ContentAdminInline, )


admin.site.register(Page, PageAdmin)


