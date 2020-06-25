from django.urls import path
from . import views

urlpatterns = [

    path('',views.lookup,name='lookup'),
    path('about',views.about,name='about'),
    path('home',views.home,name='home'),
]