from django import template
from store.models import Slider

register = template.Library()

@register.simple_tag()
def show_sliders():
    return Slider.objects.all()
