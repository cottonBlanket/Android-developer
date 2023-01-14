from django.contrib import admin
from .models import *


class ContentAdminInline(admin.StackedInline):
    model = Content
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    inlines = (ContentAdminInline,)


admin.site.register(Section, SectionAdmin)
admin.site.register(Content)


