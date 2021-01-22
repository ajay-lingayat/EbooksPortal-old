from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

def error403(request, exception):
    t = loader.get_template('errors/403.html')
    data = {'exception', exception}
    return HttpResponse(t.render(data, request))

def error404(request, exception):
    t = loader.get_template('errors/404.html')
    data = {'exception', exception}
    return HttpResponse(t.render(data, request))

def error500(request, exception):
    t = loader.get_template('errors/500.html')
    data = {}
    return HttpResponse(t.render(data, request))