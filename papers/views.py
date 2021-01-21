from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.template import loader
from .models import *
import requests
from django.core.paginator import Paginator

# Create your views here.
def papers(request, query):
    nav_actives = [None for i in range(7)]
    text = request.GET.get('query', False)

    if text:
       query = text.strip().lower()
       qlookup1 = Q(tags__name__lower=query)
       qlookup2 = Q(title__lower__contains=query)
       papers = Paper.objects.filter(qlookup1 | qlookup2).distinct().order_by('create_date')

       offset = int(request.GET.get('offset', 10))
       page_number = request.GET.get('page', 1)
       page = Paginator(papers, per_page=offset).get_page(page_number)

       Context = {
           'nav_actives': nav_actives,
           'papers': page.object_list,
           'page': page,
           'query': text,
           'offset': offset,
           'limits': [10, 25, 50, 100]
       }       
       t = loader.get_template('papers/query_papers.html')
       return HttpResponse(t.render(Context, request))
    else:
       return redirect('/papers/all')

def all(request):
    nav_actives = [None for i in range(7)]
    nav_actives[4] = 'active'

    papers = Paper.objects.all().order_by('create_date')
    offset = int(request.GET.get('offset', 10))
    page_number = request.GET.get('page', 1)
    page = Paginator(papers, per_page=offset).get_page(page_number)

    Context = {
        'nav_actives': nav_actives,
        'papers': page.object_list,
        'page': page,
        'offset': offset,
        'limits': [10, 25, 50, 100]
    }
    t = loader.get_template('papers/all_papers.html')
    return HttpResponse(t.render(Context, request))

def open_portal(request, paper):
    paper = Paper.objects.filter(id=paper)
    if paper.exists():
        Context = { 'paper': paper.first() }
        t = loader.get_template('papers/open_portal.html')
        return HttpResponse(t.render(Context, request))
    else:
       raise Http404('Paper id not provided!')

def download(request, paper):
    try:
        if paper:
            paper = paper.objects.get(id=paper)
            paper.downloads += 1
            paper.save()
            return JsonResponse({'ans': True})
        return JsonResponse({'ans': False})
    except Exception as e:
        print('Error incrementing book download')
        print(e)
        return JsonResponse({'ans': False})