from django import template
from Android_developer.models import *
register = template.Library()


@register.simple_tag()
def get_item_type(page_id, order):
    text = Text.objects.filter(page=page_id, order=order)
    if len(text) != 0:
        return 'text'
    image = Image.objects.filter(page=page_id, order=order)
    if len(image) != 0:
        return 'image'
    table = Table.objects.filter(page=page_id, order=order)
    if len(table) != 0:
        return 'table'


@register.inclusion_tag('Android-developer/content_templates/table.html')
def show_table(page_id, order):
    table = Table.objects.filter(page=page_id, order=order).first()
    headers = table.headers.strip().split(',')
    rows = table.content.strip().split('\n')
    values = [row.split(',') for row in rows]
    return {'title': table.title,
            'headers': headers,
            'values': values}


@register.inclusion_tag('Android-developer/content_templates/image.html')
def show_img(page_id, order):
    image = Image.objects.filter(page=page_id, order=order).first()
    return {'image': image}


@register.inclusion_tag('Android-developer/content_templates/text.html')
def show_text(page_id, order):
    text = Text.objects.filter(page=page_id, order=order).first()
    return {'text': text}



