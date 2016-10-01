from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from .models import Meme_pic
# Create your views here.

def index(request):
    list = Meme_pic.objects.all()[:1]
    template = loader.get_template('db_meme/index.html')
    context = {
        "items" : list
    }
    return render(request, 'db_meme/item.html', context)

def item(request):
    if request.method == 'POST':
        val1 = request.POST.CharField(label="usr")


    else:
        paramVal = request.GET.get('id','')

        if str(paramVal):
            return HttpResponseRedirect("/")

        itemElement = Meme_pic.objects.get(paramVal)
        context = {
            "item" : itemElement
        }
        return render(request, 'db_meme/item.html', context)
