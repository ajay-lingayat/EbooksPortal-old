from django.db.models import Q
from django.template import loader
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

from .models import *

import requests

# Create your views here.
def all_books(request):
    nav_actives = [None for i in range(7)]
    nav_actives[3] = 'active'

    books = Book.objects.all().order_by('create_date')
    paginator = Paginator(
        books,
        per_page=12
    )
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    Context = {
        'nav_actives': nav_actives,
        'books': page.object_list,
        'page': page,
    }
    t = loader.get_template('books/all_books.html')
    return HttpResponse(
        t.render(
            Context,
            request
        )
    )


def text(request):
    if request.method == "POST":
       txt = request.POST['q']
       return redirect(f'/books/q/{txt}')
    else:
       raise Http404()

def query(request, query):
    nav_actives = [None for i in range(7)]

    try:
        query = query.strip().lower()
    except Exception as e:
        print(e)
        query = False

    if query:
       qlookup1 = Q(tags__name__lower=query)
       qlookup2 = Q(title__lower__contains=query)
       books = Book.objects.filter(qlookup1 | qlookup2).distinct()

       paginator = Paginator(
           books.order_by('create_date'),
           per_page=12
       )
       page_number = request.GET.get('page', 1)
       page = paginator.get_page(page_number)

       Context = {
           'nav_actives': nav_actives,
           'books': page.object_list,
           'page': page,
           'query': query,
       }       
       t = loader.get_template('books/query_books.html')
       return HttpResponse(
           t.render(
               Context,
               request
           )
       )

    else:
       return redirect('/books/all')


def open_portal(request, id_no):

    if Book.objects.filter(id=id_no).exists():
        book = Book.objects.get(id=id_no)
        
        Context = {
            'book': book,
        }
        t = loader.get_template('books/open_portal.html')
        return HttpResponse(
            t.render(
                Context,
                request
            )
        )
    else:
        raise Http404()


def mark_download(request):
    try:
        book_id = request.GET.get('bk_id', False)
        ans = False
        if book_id:
            book = Book.objects.get(id=bk_id)
            book.downloads += 1
            book.save()
            ans = True
        return JsonResponse({'ans': ans})
    except Exception as e:
        print('Error incrementing book download')
        print(e)
        return JsonResponse({'ans':False})