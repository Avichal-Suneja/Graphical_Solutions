from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import models
from .models import feedback


def home(request):
    return render(request, 'home.html')

def feedback(request):


    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    models.feedback.objects.create(name = name, email = email, message = message)
    return render(request, 'myapp/feedback.html')


def order(request):
    name_o = request.POST.get('name_o')
    email_o = request.POST.get('email_o')
    message_o = request.POST.get('message_o')
    models.order.objects.create(name_o = name_o, email_o = email_o, message_o = message_o)
    return render(request, 'myapp/order.html')


def gallery(request):
    return render(request, 'myapp/gallery.html')

def faq(request):
    return render(request, 'myapp/faq.html')
