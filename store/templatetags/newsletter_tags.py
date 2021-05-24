from django import template

from store.forms import NewsLetterForm

register = template.Library()


@register.inclusion_tag("store/tags/newsletter_tpl.html")
def get_newsletter_form():
    return {"form": NewsLetterForm()}
