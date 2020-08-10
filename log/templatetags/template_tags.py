from django import template
register = template.Library()

@register.inclusion_tag("entry_button.html")
def entry_button(name, display_name, entry_id, entry_type='todo'):
    return {"name": name, "display_name": display_name, "pk": entry_id, "entry_type": entry_type}