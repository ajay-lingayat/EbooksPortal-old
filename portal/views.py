from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import *
from django.core.mail import send_mail
import os
from django.contrib.auth.models import User, auth
from books.models import *
from papers.models import *
import requests
from django.core.paginator import Paginator
from .Random import *
import random
from EbooksPortal.settings import EMAIL_HOST_USER, TO

# Create your views here.
def home( request ):
    nav_actives = [None for i in range(7)]
    nav_actives[0] = 'active'

    form = ContactForm()

    obj = book_section.objects.all()

    counter = 0

    lst = list()
    for i in obj:
        txt = i.text.lower().replace(' books', '')

        obj1 = book.objects.all()

        bks = list()
        for bk in obj1:
            
            tag_lnk = bk.tags.replace('blob', 'raw')

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
               bks.append(
                   [bk, tags_lst]
               )

            if not found and txt in bk.title.lower():
               bks.append(
                   [bk, tags_lst]
               )
        lst.append(
            [i, bks]
        )

    bk_sections = pick3(lst)

    Context = {
        'form': form,
        'nav_actives': nav_actives,
        'book_sections': bk_sections,
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