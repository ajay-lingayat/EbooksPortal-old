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
from django.conf import settings

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

    sections = BookSection.objects.all()
    sections = [[section, [[book, book.tags.all()] for book in section.books.all()]] for section in sections]
    bk_sections = pick3(sections)

    sections = PaperSection.objects.all()
    sections = [[section, [[paper, paper.tags.all()] for paper in section.papers.all()]] for section in sections]
    pr_sections = pick3(sections)

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
               settings.EMAIL_HOST_USER,
               [ settings.TO ],
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