from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback', views.feedback, name='feedback'),
    path('home', views.home, name='home'),
    path('order', views.order, name='order'),
    path('gallery', views.gallery, name='gallery'),
    path('faq', views.faq, name='faq'),
]
