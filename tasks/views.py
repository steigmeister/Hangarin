from django.shortcuts import render
from django.views.generic.list import ListView
from tasks.models import Priority

class HomePageView(ListView):
    model = Priority
    template_name = 'home.html'
    context_object_name = 'home'


