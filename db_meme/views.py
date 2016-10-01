from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

from django.template import loader
from .models import Meme_pic
# Create your views here.

def index(request):
    list = Meme_pic.objects.all()[:9]
    print(len(list))
    template = loader.get_template('db_meme/index.html')
    context = {
        "items" : list
    }
    return render(request, 'db_meme/index.html', context)

@csrf_protect
def item(request):
    if request.method == 'POST':
        val1 = request.POST.get('to_convert','')
        print(val1)
        return render(request, 'db_meme/item.html', context)

    else:
        paramVal = request.GET.get('id','')

        if str(paramVal) == '':
            return HttpResponseRedirect("/")

        itemElement = Meme_pic.objects.get(pk=paramVal)
        context = {
            "item" : itemElement
        }
        return render(request, 'db_meme/item.html', context)
