from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello world')

def page_not_found(request,exception):
    return render(request,'blog/not_found.html')
