# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    )
    host = models.CharField(max_length=100, default='theland.notroot.com')
    port = models.IntegerField(default=4000)
    profession = models.CharField(max_length=15, choices=CLASSES)

    def __str__(self):
        return self.name
