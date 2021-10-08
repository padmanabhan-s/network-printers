
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index.html'),
    path('sign-up.html',views.signUp,name='sign-up.html'),

]