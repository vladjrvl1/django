from django import template

from store.forms import SubscriberEmailForm

register = template.Library()


@register.inclusion_tag("store/tags/newsletter_tpl.html")
def get_newsletter_form():
    return {"form": SubscriberEmailForm()}
