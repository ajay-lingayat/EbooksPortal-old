from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator

import os, requests

from .forms import *
from .models import *
from .Random import *
from EbooksPortal.settings.dev import EMAIL_HOST_USER, TO

# Create your views here.
def home( request ):
    nav_actives = [None for i in range(7)]
    nav_actives[0] = 'active'

    book_downloads = 0
    for book in Book.objects.all():
        book_downloads += book.downloads

    paper_downloads = 0
    for paper in Paper.objects.all():
        paper_downloads += paper.downloads
        
    total_downloads = book_downloads+paper_downloads

    form = ContactForm()

    obj = BookSection.objects.all()
    lst = list()
    for i in obj:
        txt = i.text.lower().replace(' books', '')

        obj1 = Book.objects.all()
        bks = list()
        for book in obj1:
            tag_lnk = book.tags.replace('blob', 'raw')
            found = False
            tags_lst = list()

            r = requests.get(tag_lnk)
            if r.status_code == 200:
               tags = r.text.split('\n')
               
               for tag in tags:
                   if str(tag).strip():
                      tags_lst.append(tag)
                   if txt == str(tag).lower():
                      found = True

            if found:
               bks.append([book, tags_lst])

            if not found and txt in book.title.lower():
               bks.append([book, tags_lst])

        lst.append([i, bks])
    bk_sections = pick3(lst)

    obj = PaperSection.objects.all()
    lst = list()
    for i in obj:
        txt = i.text.lower().replace(' papers', '')

        obj1 = Paper.objects.all()
        prs = list()
        for paper in obj1:
            tag_lnk = paper.tags.replace('blob', 'raw')
            found = False
            tags_lst = list()

            r = requests.get(tag_lnk)
            if r.status_code == 200:
               tags = r.text.split('\n')
               
               for tag in tags:
                   if str(tag).strip():
                      tags_lst.append(tag)
                   if txt == str(tag).lower():
                      found = True

            if found:
               prs.append([paper, tags_lst])

            if not found and txt in paper.title.lower():
               prs.append([paper, tags_lst])
        lst.append([i, prs])

    pr_sections = pick3(lst)

    Context = {
        'form': form,
        'nav_actives': nav_actives,
        'book_sections': bk_sections,
        'paper_sections': pr_sections,
        'book_downloads': book_downloads,
        'total_downloads': total_downloads,
        'paper_downloads': paper_downloads,
    }
    t = loader.get_template('EbooksPortal/index.html')
    return HttpResponse(
        t.render(
            Context,
            request
        )
    )

def contact( request ):
    form = ContactForm()
    nav_actives = [None for i in range(7)]
    nav_actives[2] = 'active'

    if request.method == "POST":
       firstname = request.POST['firstname']
       lastname = request.POST['lastname']
       email = request.POST['email']
       subject = request.POST['subject']
       message = request.POST['message']

       mail_message = f"""
           Name : {firstname} {lastname}
           Email Address : {email}
           Message : {message}
       """

       try:
           send_mail(
               subject,
               mail_message,
               EMAIL_HOST_USER,
               [TO],
               fail_silently=False,
           )
           messages.success(
               request,
               'Message sent successfully!'
           )
       except Exception as e:
           print(e)
           messages.warning(
               request,
               'Please check you internet connection!'
           )

       Context = {
           'form': form,
           'nav_actives': nav_actives,
           'firstname': firstname,
           'lastname': lastname,
           'email': email,
           'subject': subject,
           'message': message,
       }
    else:
        Context = {
            'form': form,
            'nav_actives': nav_actives,
        }

    t = loader.get_template('EbooksPortal/contact.html')
    return HttpResponse(
        t.render(
            Context, request
        )
    )


def profile(request):
    form = ProfileForm()
    user = request.user

    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    username = user.username

    nav_actives = [None for i in range(7)]
    nav_actives[5] = 'active'

    if request.method == "POST":
       first_name = request.POST['firstname']
       last_name = request.POST['lastname']
       email = request.POST['email']
       username = request.POST['username']

       update = True

       if not first_name.isalpha():
          messages.warning(
              request,
              'Invalid firstname!'
          )
          update = False

       if not last_name.isalpha():
          messages.warning(
              request,
              'Invalid lastname!'
          )
          update = False

       if not username.isalnum() and username.isdigit():
          messages.warning(
              request,
              'Invalid username!'
          )
          update = False

       if User.objects.filter(username=username).exists() and user.username != username:
          messages.warning(
              request,
              'Username is already taken!'
          )
          update = False

       if User.objects.filter(email=email).exists() and user.email != email:
          messages.warning(
              request,
              'Email is already registered!'
          )
          update = False

       try:
           if update:
              user.first_name = first_name
              user.last_name = last_name
              user.email = email
              user.username = username
              user.save()

              messages.success(
                  request,
                  'Your profile has been updated!'
              )
       except Exception as e:
           print(e)
           messages.warning(
               request,
               'Invalid Information!'
           )

    Context ={
        'form': form,
        'nav_actives': nav_actives,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'username': username,
    }
    t = loader.get_template('EbooksPortal/profile.html')

    return HttpResponse(
        t.render(
            Context,
            request
        )
    )