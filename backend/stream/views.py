from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplate(TemplateView):
    template_name = 'index.html'