
from __future__ import unicode_literals

# Stdlib imports

# Core Django imports
from django import template
from django.template.defaulttags import register
# Third-party app imports

# Realative imports of the 'app-name' package


register = template.Library()


@register.filter('access_dict')
def access_dict(dictionary, key):
    return dictionary.get(key)

    # return True if group_name in groups else False
