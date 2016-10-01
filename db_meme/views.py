from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import Meme_pic
# Create your views here.

def index(request):
    template = loader.get_template('db_meme/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
