from django.shortcuts import render
from django.urls import path
from . import views

app_name = "pw_wowProj"

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('human', views.human_page_view, name='human'),
    path('dwarf', views.dwarf_page_view, name='dwarf'),
    path('orc', views.orc_page_view, name='orc'),
    path('troll', views.troll_page_view, name='troll'),
    path('info', views.info_page_view, name='info'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('soon', views.soon_page_view, name='soon')
]