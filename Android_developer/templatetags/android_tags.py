from django import template
from Android_developer.models import *
register = template.Library()


@register.simple_tag()
def get_content(section_id):
    content = Content.objects.filter(section=section_id)
    return content


@register.inclusion_tag('Android-developer/content_templates/section.html')
def show_section(section: Section):
    return {'section': section}


@register.inclusion_tag('../templates/Android-developer/content_templates/table.html')
def show_table(table: Content):
    content = table.content.strip().split('\n')
    headers = content[0].split(',')
    rows = content[1:]
    values = get_table_values(rows)
    return {'headers': headers,
            'values': values,
            'item': table}


def get_table_values(rows):
    result = list()
    for row in rows:
        if '[' in row and ']' in row:
            new_row = list()
            index = row.index('[')
            new_row.append(row[:index].split(',')[0])
            array = row[index:].replace('[', '').replace(']', '').replace("'", '')
            new_row.append(array)
            result.append(new_row)
        else:
            result.append(row.split(','))
    return result


@register.simple_tag()
def get_text(item: Content):
    return item.content.split('\n')


