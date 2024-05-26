from copy import deepcopy

from django.conf import settings


def _expand_field(field: dict, field_name: str, translation_mapping: dict) -> dict:
    assert field_name is not None, 'Field name cannot be None'

    if not field.get('translated', False):
        return {field_name: field}
    elif field['type'] != 'string':
        raise ValueError('Field type must be "string" to be translated')

    translation_fields = {}

    for code, language in settings.LANGUAGES:
        copy = deepcopy(field)
        copy['lang_code'] = code
        copy['original_field'] = field_name
        del copy['translated']

        if 'title' in copy:
            copy['title'] += f' ({language})'

        key = f'{field_name}_{code}'
        translation_fields[key] = copy
        translation_mapping[key] = field_name

    return translation_fields


def expand_schema_translation(schema: dict, name: str = None, translation_mapping: dict = None) -> dict:
    if translation_mapping is None:
        translation_mapping = {}

    type_ = schema.get('type')

    if type_ in ('array', 'list'):
        assert name is not None, 'name must be defined for types other than object and dict'

        if schema['items'].get('translated', False):
            raise ValueError('Array/List item cannot be translated. Use nested object instead')

        schema['items'] = expand_schema_translation(schema['items'], translation_mapping=translation_mapping)
        return {name: schema}

    elif type_ in ('object', 'dict'):
        keys = {}

        for field_name, field in schema['keys'].items():
            expanded_fields = expand_schema_translation(field, field_name, translation_mapping=translation_mapping)
            for key, val in expanded_fields.items():
                keys[key] = val

        schema['keys'] = keys

        return {name: schema} if name is not None else schema

    else:
        assert name is not None, 'name must be defined for types other than object and dict'
        return _expand_field(schema, name, translation_mapping=translation_mapping)


def get_translation_mapping(schema):
    mapping = {}
    schema = deepcopy(schema)
    expand_schema_translation(schema, translation_mapping=mapping)
    return mapping


def substitute_translation(data: dict, translation_mapping: dict, lang_code: str):
    new_data = {}

    for key, value in data.items():
        if isinstance(value, dict):
            new_data[key] = substitute_translation(value, translation_mapping, lang_code)

        elif isinstance(value, list):
            new_data[key] = [substitute_translation(item, translation_mapping, lang_code)
                             for item in value]
        else:
            if key in translation_mapping:
                if key.endswith(lang_code):
                    field_name = translation_mapping[key]
                    new_data[field_name] = value
            else:
                new_data[key] = value

    return new_data
