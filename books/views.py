from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import *
import requests
from django.core.paginator import Paginator

# Create your views here.
def all_books(request):
    nav_actives = [None for i in range(7)]
    nav_actives[3] = 'active'

    obj = book.objects.all()

    books = list()
    for i in obj:
        lst = [i]
        lst1 = list()

        tags_lnk = i.tags.replace('blob', 'raw')

        r = requests.get(tags_lnk)

        if r.status_code == 200:
           r = r.text
           r = r.split('\n')
           for tag in r:
               if tag.replace(' ', ''):
                  lst1.append(tag)

        lst.append(lst1)
        books.append(lst)

    paginator = Paginator(
        books,
        per_page=10
    )
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    Context = {
        'nav_actives': nav_actives,
        'books': page.object_list,
        'page': page,
    }
    t = loader.get_template('EbooksPortal/all_books.html')
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
       raise Http404('')

def query(request, query):
    nav_actives = [None for i in range(7)]

    try:
        query = query.strip().lower()
    except Exception as e:
        print(e)
        query = False

    if query:
       
       obj = book.objects.all()

       books = list()
       for bk in obj:
           tags_lnk = bk.tags.replace('blob', 'raw')

           r = requests.get(tags_lnk)
           if r.status_code == 200:
              r = r.text
              tags = r.split('\n')

              found = False
              for tag in tags:
                  tag = tag.strip()
                  if query == tag.lower():
                     books.append(bk)
                     found = True

           if not found and query in bk.title.lower():
              books.append(bk)

       
       bks = list()
       for i in books:
           lst = [i]
           lst1 = list()

           tags_lnk = i.tags.replace('blob', 'raw')

           r = requests.get(tags_lnk)

           if r.status_code == 200:
              r = r.text
              r = r.split('\n')
              for tag in r:
                  if tag.replace(' ', ''):
                     lst1.append(tag)

           lst.append(lst1)
           bks.append(lst)

       paginator = Paginator(
           bks,
           per_page=10
       )
       page_number = request.GET.get('page', 1)
       page = paginator.get_page(page_number)

       Context = {
           'nav_actives': nav_actives,
           'books': page.object_list,
           'page': page,
           'query': query,
       }       
       t = loader.get_template('EbooksPortal/query_books.html')
       return HttpResponse(
           t.render(
               Context,
               request
           )
       )

    else:
       return redirect('/books/all')


def open_portal(request, id_no):

    obj = book.objects.get(id=id_no)

    bk = [obj, []]
    tags_lnk = obj.tags.replace('blob', 'raw')

    r = requests.get(tags_lnk)

    if r.status_code == 200:
        r = r.text
        r = r.split('\n')
        for tag in r:
            if tag.replace(' ', ''):
                bk[1].append(tag)
    
    Context = {
        'book': bk,
    }
    t = loader.get_template('EbooksPortal/open_portal.html')
    return HttpResponse(
        t.render(
            Context,
            request
        )
    )