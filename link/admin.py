# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Psychic

# Register your models here.
class PsychicAdmin(admin.ModelAdmin):
    fields = ['name', 'profession', 'host', 'port']

admin.site.register(Psychic, PsychicAdmin)
