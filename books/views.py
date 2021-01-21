from django.db.models import Q
from django.template import loader
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

from .models import *

import requests

# Create your views here.
def books(request):
    nav_actives = [None for i in range(7)]
    text = request.GET.get('query', False)

    if text:
       query = text.strip().lower()
       qlookup1 = Q(tags__name__lower=query)
       qlookup2 = Q(title__lower__contains=query)
       books = Book.objects.filter(qlookup1 | qlookup2).distinct().order_by('create_date')

       offset = int(request.GET.get('offset', 10))
       page_number = request.GET.get('page', 1)
       page = Paginator(books, per_page=offset).get_page(page_number)

       Context = {
           'nav_actives': nav_actives,
           'books': page.object_list,
           'page': page,
           'query': text,
           'offset': offset,
           'limits': [10, 25, 50, 100]
       }       
       t = loader.get_template('books/query_books.html')
       return HttpResponse(t.render(Context, request))
    else:
       return redirect('/books/all/')
       
def all(request):
    nav_actives = [None for i in range(7)]
    nav_actives[3] = 'active'

    offset = int(request.GET.get('offset', 10))
    page_number = request.GET.get('page', 1)
    books = Book.objects.all().order_by('create_date')
    page = Paginator(books, per_page=offset).get_page(page_number)

    Context = {
        'nav_actives': nav_actives,
        'books': page.object_list,
        'page': page,
        'offset': offset,
        'limits': [10, 25, 50, 100]
    }
    t = loader.get_template('books/all_books.html')
    return HttpResponse(t.render(Context, request))

def open_portal(request, book):
    book = Book.objects.filter(id=book)
    if book.exists():
        Context = {'book': book.first()}
        t = loader.get_template('books/open_portal.html')
        return HttpResponse(t.render(Context, request))
    else:
        raise Http404('Book id not provided!')

def download(request, book):
    try:
        if book:
            book = Book.objects.get(id=book)
            book.downloads += 1
            book.save()
            return JsonResponse({'ans': True})
        return JsonResponse({'ans': False})
    except Exception as e:
        print('Error incrementing book download')
        print(e)
        return JsonResponse({'ans': False})