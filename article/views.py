from article.producer import publish
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(requests):
    publish()
    return HttpResponse('Hello article')
