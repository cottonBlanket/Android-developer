from django import template
from Android_developer.models import *
register = template.Library()


@register.simple_tag()
def get_item_type(page_id, order):
    content = Content.objects.get(page=page_id, order=order)
    return content.content_type


@register.inclusion_tag('Android-developer/content_templates/table.html')
def show_table(page_id, order):
    table = Content.objects.filter(page=page_id, order=order).first()
    content = table.content.strip().split('\n')
    headers = content[0].split(',')
    rows = content[1:]
    values = [row.split(',') for row in rows]
    return {'title': table.title,
            'headers': headers,
            'values': values}


@register.inclusion_tag('Android-developer/content_templates/image.html')
def show_img(page_id, order):
    image = Content.objects.get(page=page_id, order=order)
    return {'image': image}


@register.inclusion_tag('Android-developer/content_templates/text.html')
def show_text(page_id, order):
    text = Content.objects.get(page=page_id, order=order)
    return {'text': text}



