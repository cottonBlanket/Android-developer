from django import template
from Android_developer.models import *
register = template.Library()


@register.simple_tag()
def get_content(section_id):
    content = Content.objects.filter(section=section_id)
    return content


@register.simple_tag()
def get_styles(item_id):
    try:
        styles = Style.objects.get(content_id=item_id)
        return styles
    except:
        return None


@register.inclusion_tag('Android-developer/section.html')
def show_section(section: Section):
    return {'section': section}


@register.inclusion_tag('../templates/Android-developer/content_templates/table.html')
def show_table(table: Content):
    content = table.content.strip().split('\n')
    headers = content[0].split(',')
    rows = content[1:]
    values = [row.split(',') for row in rows]
    return {'headers': headers,
            'values': values,
            'item': table}


