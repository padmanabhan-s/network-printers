from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login/")
def index(request):
    context = {}
    html_template = loader.get_template("index.html" )
    return HttpResponse(html_template.render(context, request))
    #return render(request, "index.html")






def signUp(request):
    context = {}
    html_template = loader.get_template("sign-up.html" )
    return HttpResponse(html_template.render(context, request))

