from django import template
from pages.models import Page

# registré una función normal en un simple tag simple en un template
register = template.Library()


@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
