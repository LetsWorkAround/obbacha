'''
To render html web pages
'''
from tkinter import ARC
from django.http import HttpResponse
from django.template.loader import render_to_string

def home_view(request):

    context = {
    }

    # Django Templates

    HTML_STRING = render_to_string("home-view.html")

    return HttpResponse(HTML_STRING)