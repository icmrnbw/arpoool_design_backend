from pprint import pprint

from apps.settings.services import get_settings
from apps.settings.translation_utils import substitute_translation, get_translation_mapping


def settings_processor(request):
    settings = {obj.key: substitute_translation(obj.data, get_translation_mapping(obj.schema), request.LANGUAGE_CODE)
                for obj in get_settings()}

    return {
        'settings': settings
    }
