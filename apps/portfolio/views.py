from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import activate

from apps.portfolio.filters import ProjectFilter
from apps.portfolio.forms import InquiryForm
from apps.portfolio.models import Project, Service, Client


def switch_language(request, lang_code):
    activate(lang_code)
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response


def portfolio_view(request):
    queryset = Project.objects.all()
    filterset = ProjectFilter(request.GET, queryset=queryset)
    projects = filterset.qs
    rearranged_projects = []
    i = 0
    while i < len(projects):
        if i % 3 == 0:
            rearranged_projects.append((projects[i],))
        else:
            if i + 1 < len(projects):
                rearranged_projects.append((projects[i], projects[i + 1]))
                i += 1
            else:
                rearranged_projects.append((projects[i],))
        i += 1
    services = Service.objects.all()
    return render(request, 'portfolio.html', {
        'filterset': filterset,
        'projects': rearranged_projects,
        'services': services
    })


def index_view(request):
    clients = Client.objects.all()
    projects = Project.objects.all().order_by('-created_at')[:5]
    services = Service.objects.all()
    return render(request, 'index.html', {'projects': projects, 'services': services, 'clients': clients})


def contact_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InquiryForm()
    return render(request, 'contact.html', {'form': form})


def portfolio_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    projects = Project.objects.exclude(pk=pk)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InquiryForm()
    return render(request, 'portfolio_detail.html', {'project': project, 'projects': projects,
                                                     'form': form})


def service_detail_view(request, pk):
    service = get_object_or_404(Service, pk=pk)
    services = Service.objects.exclude(pk=pk)
    projects = Project.objects.all().order_by('-created_at')
    context = {
        'service': service,
        'services': services,
        'projects': projects,
    }
    return render(request, 'service_detail.html', context)


def inquiry_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InquiryForm()
    return render(request, 'project_inquiry.html', {'form': form})


def handler404_view(request, exception):
    return render(request, '404.html', {}, status=404)
