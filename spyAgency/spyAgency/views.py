from django.shortcuts import render
from django.views.generic import TemplateView


class Error403View(TemplateView):
    template_name = '403.html'


class Error404View(TemplateView):
    template_name = '403.html'
