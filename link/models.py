# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Psychic(models.Model):
    name = models.CharField(max_length=30)
    CLASSES = (
        ('S', 'p(S)ychic'),
        ('W', '(W)arrior'),
        ('T', '(T)hief'),
        ('M', '(M)age'),
        ('C', '(C)leric'),
        ('K', 'Mon(K)'),
        ('P', '(P)aladin'),
        ('D', '(D)ruid'),
    )
    profession = models.CharField(max_length=1, choices=CLASSES)
    host = models.CharField(max_length=100, default='theland.notroot.com')
    port = models.IntegerField(default=4000)

    def __str__(self):
        return self.name
