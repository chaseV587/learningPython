from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from blog import models


def hello(request):
    return HttpResponse('Hello,world')


def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    context = {
        'blog_index' : blog_index
    }
    return render(request, 'index.html', context)

