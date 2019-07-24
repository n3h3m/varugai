import os

from django.conf.urls import url
from django.http import HttpResponse

from app.settings import ALLOWED_EXTENSIONS

def static(path):
    filename = os.path.basename(path)
    if '.' not in filename:
        path += '/index.html'

    extension = path.split('.')[-1]
    if extension not in ALLOWED_EXTENSIONS:
        return "Forbidden", 403, 'text/html'

    if extension == 'ico':
        content_type = 'image/x-icon'
    elif extension in ['jpg', 'jpeg']:
        content_type = 'image/jpeg'
    elif extension in ['js']:
        content_type = 'text/javascript'
    elif extension in ['font', 'css']:
        content_type = 'text/css'
    elif extension in ['js']:
        content_type = 'text/javascript'
    elif extension in ['html']:
        content_type = 'text/html'

    try:
        with open('www/' + path, 'rb') as f:
            return f.read(), 200, content_type
    except FileNotFoundError:
        return "Not found", 404, 'text/html'

def www(req):
    path = req.path.strip('/')
    content, status, content_type = static(path)
    return HttpResponse(content, status=status, content_type=content_type)

urlpatterns = [
    url('', www)
]
