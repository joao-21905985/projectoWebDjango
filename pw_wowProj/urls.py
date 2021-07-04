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
    path('soon', views.soon_page_view, name='soon'),
    path('feedback', views.contactos_page_view, name='feedback'),
    path('registo', views.registo_page_view, name='registo'),
    path('journal', views.journal_view, name='journal'),
    path('raid/<int:raid_id>', views.raid_view, name='raid')


]