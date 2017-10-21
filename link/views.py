"""
Definition of views.
"""

from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from django.template import RequestContext
from .models import Psychic

import datetime
import os
import pexpect
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

def telnet(request):

    link = get_object_or_404(Psychic, pk=1)
    password = 'wabiwabi'

    host = 'theland.notroot.com'
    port = 5000

    child = pexpect.spawn('telnet ' + str(host) + " " + str(port))
    i = child.expect([pexpect.TIMEOUT, 'None'])
    if i == 0:
        return render(request, 'app/link.html')
    if i == 1:
        link.connect_attempt = 'HIT'
        child.sendline('link')
        child.expect ('(?i)password')
