# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.
class Psychic(models.Model):
    name = models.CharField(max_length=30)
    CLASSES = (
        ("p(S)ychic", 'S'),
        ("(W)arrior", 'W'),
        ("(T)hief", 'T'),
        ("(M)age", 'M'),
        ("(C)leric", 'C'),
        ("Mon(K)", 'K'),
        ("(P)aladin", 'P'),
        ("(D)ruid", 'D'),
        ("(Tr)raveller", 'Traveller'),
        ("Jack of Clubs", 'Joker'),
    )
    ATTEMPT_RESULT = (
        ("HIT", 'HIT'),
        ("MISS", 'MISS'),
    )
    host = models.CharField(max_length=100, default='theland.notroot.com')
    port = models.IntegerField(default=4000)
    profession = models.CharField(max_length=15, choices=CLASSES)
    connect_attempt = models.CharField(max_length=15, choices=ATTEMPT_RESULT, blank=True)

    def __str__(self):
        return self.name

class Update(models.Model):
    owner = models.CharField(max_length=60, blank=True)
    event = models.CharField(max_length=150)
    post_date = models.DateField("Date", default=datetime.date.today)
