from django.contrib import admin
from .models import *


class StyleAdminInline(admin.StackedInline):
    model = Style
    extra = 1


class ContentAdmin(admin.ModelAdmin):
    inlines = (StyleAdminInline,)


class ContentAdminInline(admin.StackedInline):
    model = Content
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    inlines = (ContentAdminInline,)


class SectionAdminInline(admin.StackedInline):
    model = Section
    extra = 1


class PageAdmin(admin.ModelAdmin):
    inlines = (SectionAdminInline,)


admin.site.register(Page, PageAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Style)


