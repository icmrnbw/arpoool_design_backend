from pprint import pprint

from apps.settings.services import get_settings
from apps.settings.translation_utils import substitute_translation, get_translation_mapping


def group_items_in_pairs(items):
    """ Group items in pairs (tuples). """
    items_list = list(items)
    grouped_items = [(items_list[i], items_list[i + 1] if i + 1 < len(items_list) else None)
                     for i in range(0, len(items_list), 2)]
    return grouped_items


def settings_processor(request):
    settings = {obj.key: substitute_translation(obj.data, get_translation_mapping(obj.schema), request.LANGUAGE_CODE)
                for obj in get_settings()}
    if 'index' in settings and 'know_more' in settings['index'] and 'cards' in settings['index']['know_more']:
        cards = settings['index']['know_more']['cards']
        grouped_cards = group_items_in_pairs(cards)
        settings['index']['know_more']['grouped_cards'] = grouped_cards
    return {
        'settings': settings
    }
