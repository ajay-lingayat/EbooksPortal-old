from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader


def error403(request, exception):
    t = loader.get_template('errors/403.html')
    return HttpResponse(
        t.render(
            {},
            request
        )
    )

def error404(request, exception):
    t = loader.get_template('errors/404.html')
    return HttpResponse(
        t.render(
            {},
            request
        )
    )

def error500(request):
    t = loader.get_template('errors/500.html')
    return HttpResponse(
        t.render(
            {},
            request
        )
    )