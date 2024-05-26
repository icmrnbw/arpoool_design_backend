from apps.settings.services import get_settings


def settings_processor(request):
    settings = {obj.key: obj.data
                for obj in get_settings()}

    return {
        'settings': settings
    }
