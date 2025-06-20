from django import template

register = template.Library()

@register.filter
def tamanho_legivel(value):
    try:
        value = int(value)
        if value >= 1048576:
            return f"{value / 1048576:.2f} MB"
        elif value >= 1024:
            return f"{value / 1024:.1f} KB"
        else:
            return f"{value} B"
    except:
        return "0 B" 