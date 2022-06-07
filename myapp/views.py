from django.shortcuts import render
from django.http import HttpResponse

def one(request):
    message = '<h1>One</h1>'
    return HttpResponse(message)

def two(request):
    message = '<h1>Two</h1>'
    return HttpResponse(message)

def three(request):
    message = '<h1>Three</h1>'
    return HttpResponse(message)


# Create your views here.
