"""
Definition of views.
"""

from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from django.template import RequestContext
from .models import Psychic

import datetime
import os
import telnetlib

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
            'title': 'What is this?',
            'message': "This is a switching and control center for a guild of players operating in a virtual gaming environment.",
        },
    )

def link(request):
    """
    Renders Link's AutoBot
    """
    assert isinstance(request, HttpRequest)
    link = get_object_or_404(Psychic, pk=1)

    return render(
        request,
        'app/link.html',
        {
            'link': link,
            'title': "Link's Humble Abode",
            'message': 'If you do not know what is happening here, rememeber you can ask.',
            'host': link.host,
            'port': link.port,
            'telnet': telnet,
        },
    )

def telnet():

    link = get_object_or_404(Psychic, pk=1)
    password = 'wabiwabi'

    try:
        s = telnetlib.Telnet(link.host, link.port)
        s.set_debuglevel(9)

        try:
            s
        except:
            print 'Unable to connect'
            os.sys.exit()

        print 'Connected!'
    except:
        print("Exception was thrown")
        print("debug information:")
        print(str(s))
    if s == 0:
        print ("TIMED OUT")
    if s == 1:
        link.data = s.read_until("By what name do you wish to be known?")
        return link.data
        s.close()
