from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.template import loader
from .models import *
import requests
from django.core.paginator import Paginator

# Create your views here.
def all_papers(request):
    nav_actives = [None for i in range(7)]
    nav_actives[4] = 'active'

    papers = Paper.objects.all().order_by('create_date')

    paginator = Paginator(
        papers,
        per_page=12
    )
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    Context = {
        'nav_actives': nav_actives,
        'papers': page.object_list,
        'page': page,
    }
    t = loader.get_template('papers/all_papers.html')
    return HttpResponse(
        t.render(
            Context,
            request
        )
    )


def text(request):
    if request.method == "POST":
       txt = request.POST['q']
       return redirect(f'/papers/q/{txt}')
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
       papers = Paper.objects.filter(qlookup1 | qlookup2).distinct()

       paginator = Paginator(
           papers.order_by('create_date'),
           per_page=12
       )
       page_number = request.GET.get('page', 1)
       page = paginator.get_page(page_number)

       Context = {
           'nav_actives': nav_actives,
           'papers': page.object_list,
           'page': page,
           'query': query,
       }       
       t = loader.get_template('papers/query_papers.html')
       return HttpResponse(
           t.render(
               Context,
               request
           )
       )

    else:
       return redirect('/papers/all')


def open_portal(request, id_no):
    if Paper.objects.filter(id=id_no).exists():
        Context = { 'paper': Paper.objects.get(id=id_no) }
        t = loader.get_template('papers/open_portal.html')
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
        paper_id = request.GET.get('paper_id', False)
        ans = False
        if paper_id:
            paper = paper.objects.get(id=paper_id)
            paper.downloads += 1
            paper.save()
            ans = True
        return JsonResponse({'ans':ans})
    except Exception as e:
        print('Error incrementing book download')
        print(e)
        return JsonResponse({'ans':False})