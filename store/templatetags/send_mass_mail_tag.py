from django import template

from store.forms import MassMailForm

register = template.Library()


@register.inclusion_tag("store/tags/sendmassmail_tpl.html")
def send_mass_mail():
    return {"form": MassMailForm()}
