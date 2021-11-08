from django.shortcuts import render
from .models import File
from accounts.models import CustomUser
import json
from django.http import JsonResponse


def editor(request):
    return render(request, 'editor/editor.html')

def save_file(request):
    body = json.loads(request.body)

    print(body)

    return JsonResponse({ 'status': 'OK' })
