# coding=utf-8

from django.views.decorators.http import require_GET
from django.http import HttpResponse

@require_GET
def index(request):
    return HttpResponse("hello bomb")
