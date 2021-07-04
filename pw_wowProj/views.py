from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Feedback, Raid, Raider

# Create your views here.
from django.urls import reverse

from pw_wowProj.form import ContactoForm


def index_page_view(request):
    return render(request, 'pw_wowProj/index.html')


def human_page_view(request):
    context = {
        'background': "blueback",
        'headercolor': "allyheader"
    }
    return render(request, 'pw_wowProj/human.html', context)


def dwarf_page_view(request):
    context = {
        'background': "blueback",
        'headercolor': "allyheader"
    }
    return render(request, 'pw_wowProj/dwarf.html', context)


def orc_page_view(request):
    context = {
        'background': "redback",
        'headercolor': "hordeheader"
    }
    return render(request, 'pw_wowProj/orc.html', context)


def troll_page_view(request):
    context = {
        'background': "redback",
        'headercolor': "hordeheader"
    }
    return render(request, 'pw_wowProj/troll.html', context)


def info_page_view(request):
    return render(request, 'pw_wowProj/info.html')


def soon_page_view(request):
    return render(request, 'pw_wowProj/soon.html')


def quizz_page_view(request):
    return render(request, 'pw_wowProj/quizz.html')


def contactos_page_view(request):
    #isto é a feedback page, caguei em mudar o nome
    if request.method=='POST':
        feedback=Feedback()
        feedback.feedbackName=request.POST.get('name')
        feedback.feedbackEmail=request.POST.get('email')
        feedback.feedbackSubject=request.POST.get('subject')
        feedback.save()
        return HttpResponseRedirect(reverse('pw_wowProj:index'))
    return render(request, 'pw_wowProj/contactos.html')



def registo_page_view(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('pw_wowProj:info'))

    context = {'form': form}
    return render(request, 'pw_wowProj/registo.html',context)

def journal_view(request):
    return render(request, 'pw_wowProj/journal.html', {
        'raid': Raid.objects.all()
    })

def raid_view(request, raid_id):
    r = Raid.objects.get(pk=raid_id)
    return render(request, "pw_wowProj/raid.html", {
        "raid": r,
        "raiders": r.Raiders.all(),
        "benched": Raider.objects.exclude(raids=r)
    })