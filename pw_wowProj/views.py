from django.shortcuts import render
import datetime


# Create your views here.
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