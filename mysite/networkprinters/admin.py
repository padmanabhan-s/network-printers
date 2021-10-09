# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from .models import FeedbackForm,  User,Profile

# Register your models here.



admin.site.register(Profile)



admin.site.register(FeedbackForm)