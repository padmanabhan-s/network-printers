from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    context = {}
    html_template = loader.get_template("index.html" )
    return HttpResponse(html_template.render(context, request))

def signUp(request):
    context = {}
    html_template = loader.get_template("sign-up.html" )
    return HttpResponse(html_template.render(context, request))

