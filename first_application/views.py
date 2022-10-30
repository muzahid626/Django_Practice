from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from first_application import models

# Create your views here.

# function base view
# def index_test(request):
#     return HttpResponse("Hello World")

# class base view
# class IndexView(View):
#     def get(self, request):
#         return HttpResponse("Hello World")


class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/index.html'


class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'first_app/musician_details.html'
