from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    params_dict = context['request'].GET.copy()
    for key, value in kwargs.items():
        params_dict[key] = value
    for key in [key for key, value in params_dict.items() if not value]:
        del params_dict[key]
    return params_dict.urlencode()
