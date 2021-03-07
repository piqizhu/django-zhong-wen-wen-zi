from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import 文章

def home(request):
    文 = 文章.objects.get(id=1)
    拼接 = f"{文.id},{文.标题},{文.内容}"
    return HttpResponse(拼接)