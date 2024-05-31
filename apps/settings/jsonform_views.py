from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse


@login_required
def file_handler_view(request):
    if not request.user.is_staff:
        raise PermissionDenied()

    fs = FileSystemStorage()
    BASE_PATH = Path('videos')

    if request.method == 'POST':
        file = request.FILES['file']
        filename = fs.save(BASE_PATH / file.name, file)
        file_url = fs.url(filename)
        return JsonResponse({'value': file_url})
    elif request.method == 'GET':
        path = Path(fs.location) / 'videos'
        results = []

        if path.exists():
            for file in path.iterdir():
                results.append({'value': fs.url(BASE_PATH / file.name),
                                'metadata': {'name': file.name}})

        return JsonResponse({'results': results})

    elif request.method == 'DELETE':
        file_names = request.GET.getlist('value')

        for name in file_names:
            name = name.replace('/media/', '')
            fs.delete(name)

        return HttpResponse(status=204)
