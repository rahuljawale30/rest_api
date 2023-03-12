from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello this is ewebsite')

def about(request):
    return HttpResponse('hello this is about')

def contact(request):
    return HttpResponse('hello this is contact')

def tracker(request):
    return HttpResponse('hello this is tracker')

def search(request):
    return HttpResponse('hello this is search')

def productview(request):
    return HttpResponse('hello this is product')

def checkout(request):
    return HttpResponse('hello this is checkou')



