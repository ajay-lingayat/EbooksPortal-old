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

    obj = paper.objects.all()

    papers = list()
    for i in obj:
        lst = [i]
        lst1 = list()

        downloads = len(paper_download.objects.filter(paper=i.id))

        tags_lnk = i.tags.replace('blob', 'raw')

        r = requests.get(tags_lnk)

        if r.status_code == 200:
           r = r.text
           r = r.split('\n')
           for tag in r:
               if tag.replace(' ', ''):
                  lst1.append(tag)

        lst.append(lst1)
        lst.append(downloads)
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
       
       obj = paper.objects.all()

       papers = list()
       for pr in obj:
           tags_lnk = pr.tags.replace('blob', 'raw')

           r = requests.get(tags_lnk)
           if r.status_code == 200:
              r = r.text
              tags = r.split('\n')

              found = False
              for tag in tags:
                  tag = tag.strip()
                  if query == tag.lower():
                     papers.append(pr)
                     found = True

           if not found and query in pr.title.lower():
              papers.append(pr)

       
       prs = list()
       for i in papers:
           lst = [i]
           lst1 = list()

           dowloads = len(paper_download.objects.filter(paper=i.id))

           tags_lnk = i.tags.replace('blob', 'raw')

           r = requests.get(tags_lnk)

           if r.status_code == 200:
              r = r.text
              r = r.split('\n')
              for tag in r:
                  if tag.replace(' ', ''):
                     lst1.append(tag)

           lst.append(lst1)
           lst.append(dowloads)
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

    if paper.objects.filter(id=id_no).exists():
        obj = paper.objects.get(id=id_no)

        pr = [obj, []]

        dowloads = len(paper_download.objects.filter(paper=obj.id))
        pr.append(dowloads)

        tags_lnk = obj.tags.replace('blob', 'raw')

        r = requests.get(tags_lnk)

        if r.status_code == 200:
            r = r.text
            r = r.split('\n')
            for tag in r:
                if tag.replace(' ', ''):
                    pr[1].append(tag)
        
        Context = {
            'paper': pr,
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

    paper_id = request.GET.get('paper_id', None)
    
    ans = False

    try:
        if paper_id is not None:
            pr = paper.objects.get(id=paper_id)
            obj = paper_download.objects.create(paper=pr)
            obj.save()
            ans = True
    except Exception as e:
        print(e)

    data = {
        'ans': ans,
    }
    return JsonResponse(data)