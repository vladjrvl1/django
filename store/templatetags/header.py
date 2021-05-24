from django import template
from store.models import Category

register = template.Library()

@register.inclusion_tag('store/tags/header_tpl.html')
def show_header():
    categories = Category.objects.all()
    return {"categories": categories}
