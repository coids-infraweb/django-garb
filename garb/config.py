from django.contrib.admin import ModelAdmin
from django.conf import settings


def default_config():
    return {
        # configurable
        'PROJECT_NAME': 'Django Garb',
        'HEADER_DATE_FORMAT': 'l, jS F Y',
        'HEADER_TIME_FORMAT': 'H:i',
        'LIST_PER_PAGE': 10,
        'MENU': [],
    }


def get_config(param=None):
    config_key = 'GARB_CONFIG'
    if hasattr(settings, config_key):
        config = getattr(settings, config_key, {})
    else:
        config = default_config()
    if param:
        value = config.get(param)
        if value is None:
            value = default_config().get(param)
        return value
    return config

# Reverse default actions position
ModelAdmin.actions_on_top = False
ModelAdmin.actions_on_bottom = True

# Set global list_per_page
ModelAdmin.list_per_page = get_config('LIST_PER_PAGE')
