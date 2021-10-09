
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index.html'),
    path('sign-up.html',views.signUp,name='sign-up.html'),
    
    path('about-us.html',views.aboutUs,name='about-us.html'),
    path('feedback-form.html',views.feedbackForm,name='feedback-form.html'),
    path('privacy-policy.html',views.privacyPolicy,name='privacy-policy.html'),
    
     # Profile
    path('profile',views.profile,name='profile'),

]