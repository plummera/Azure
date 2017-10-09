"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """
    Renders the home page.
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
    )

def contact(request):
    """
    Renders the contact page.
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
    )

def about(request):
    """
    Renders the about page.
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'Gnu #, who dis?',
            'message': "This is just a nonsense app flexin' on Azure",
        },
    )

def link(request):
    """
    Renders Link's AutoBot
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/link.html',
        {
            'name': 'Link',
            'host': 'theland.notroot.com',
            'port': '4000',
            'title': "Link's Humble Abode",
            'message': 'If you do not know what is happening here, rememeber you can ask.',
        },
    )
