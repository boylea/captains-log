from django import template
register = template.Library()

@register.inclusion_tag("entry_button.html")
def entry_button(name, display_name, entry_id):
    return {"name": name, "display_name": display_name, "pk": entry_id}