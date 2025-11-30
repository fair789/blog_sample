from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Blog Index')

def detail(request, article_id):
    return HttpResponse('Article: {}'.format(article_id))

def update(request, article_id):
    return HttpResponse('article_id: {}'.format(article_id))
