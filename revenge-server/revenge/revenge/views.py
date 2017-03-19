# coding=utf-8


from django.views.decorators.http import require_GET
from django.http import HttpResponse

@require_GET
def home(request):
    user = request.user
    return HttpResponse("hello world")

