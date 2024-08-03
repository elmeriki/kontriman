from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count,Sum
from django.db.models import Q
import datetime
from datetime import datetime
from datetime import date
import threading
from django.db import transaction
from django.conf import settings




def welcome_home(request):
    return render(request,'web/index.html')


def contactView(request):
    return render(request,'web/contact.html')



def aboutView(request):
    return render(request,'web/about.html')


def downloadView(request):
    return render(request,'web/download.html')


def how_does_it_worksView(request):
    return render(request,'web/how_it_works.html')

def privacy_termsView(request):
    return render(request,'web/privacy_terms.html')