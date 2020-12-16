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

    obj = Paper.objects.all()
    papers = list()
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
        papers.append(lst)

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
       obj = Paper.objects.all()
       papers = list()
       for paper in obj:
           tags_lnk = paper.tags.replace('blob', 'raw')

           r = requests.get(tags_lnk)
           if r.status_code == 200:
              r = r.text
              tags = r.split('\n')

              found = False
              for tag in tags:
                  tag = tag.strip()
                  if query == tag.lower():
                     papers.append(paper)
                     found = True

           if not found and query in paper.title.lower():
              papers.append(paper)

       prs = list()
       for i in papers:
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
           prs.append(lst)

       paginator = Paginator(
           prs,
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
        obj = Paper.objects.get(id=id_no)
        paper = [obj, []]

        tags_lnk = obj.tags.replace('blob', 'raw')

        r = requests.get(tags_lnk)
        if r.status_code == 200:
            r = r.text
            r = r.split('\n')
            for tag in r:
                if tag.replace(' ', ''):
                    paper[1].append(tag)
        
        Context = {
            'paper': paper,
        }
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