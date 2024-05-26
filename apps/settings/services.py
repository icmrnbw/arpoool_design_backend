from apps.settings.models import SiteSetting


def get_settings():
    return SiteSetting.objects.all()
