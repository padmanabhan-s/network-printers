from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib import messages

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






def aboutUs(request):
    context = {}
    html_template = loader.get_template("about-us.html" )
    return HttpResponse(html_template.render(context, request))
def feedbackForm(request):
    context = {}
    html_template = loader.get_template("feedback-form.html" )
    return HttpResponse(html_template.render(context, request))
def privacyPolicy(request):
    context = {}
    html_template = loader.get_template("privacy-policy.html" )
    return HttpResponse(html_template.render(context, request))


def profile(request):
    profile_form = request.user.profile
    form = ProfileForm(instance=profile_form)
    context = {'form':form}
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile_form)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Profile Updated Successfuly !!!')
            context = {}
            html_template = loader.get_template( 'index.html' )
            return HttpResponse(html_template.render(context, request))
    html_template = loader.get_template( 'profile.html' )
    return HttpResponse(html_template.render(context, request))
