from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import path
from . import views

class HomePageView(TemplateView):
    template_name = 'home.html'

