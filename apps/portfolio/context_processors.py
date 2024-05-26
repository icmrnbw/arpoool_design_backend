from apps.portfolio.models import Service, SiteSettings


def services_processor(request):
    services = Service.objects.all()
    context = {'services': services}
    return context


def socials_processor(request):
    settings = SiteSettings.objects.first()
    if not settings:
        return {}
    socials = settings.socials
    phone = settings.phone
    email = settings.email
    telegram = settings.telegram
    print(phone)
    return {'socials': socials, 'phone': phone, 'email': email, 'telegram': telegram}
