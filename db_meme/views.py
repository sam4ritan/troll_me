from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

from django.template import loader
from .models import Meme_pic
from .linker import link_creator
# Create your views here.

def index(request):
    list = Meme_pic.objects.all()[:9]
    template = loader.get_template('db_meme/index.html')
    context = {
        "items" : list
    }
    return render(request, 'db_meme/index.html', context)

@csrf_protect
def item(request):
    val1 = ''

    if request.method == 'POST':
        val1 = request.POST.get('to_convert','')
        bildid = request.POST.get('bildid','')
    else:
        bildid = request.GET.get('id','')

    if str(bildid) == '':
        return HttpResponseRedirect("/")

    itemElement = Meme_pic.objects.get(pk=bildid)

    convertText = ''
    if len(str(val1)) > 0:
        convertText = link_creator(val1, itemElement.murl)

    context = {
        'item' : itemElement,
        'copytext' : convertText
    }
    return render(request, 'db_meme/item.html', context)
