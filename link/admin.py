# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Psychic
from .models import Update

# Register your models here.
class PsychicAdmin(admin.ModelAdmin):
    fields = ['name', 'host', 'port', 'profession', 'connect_attempt']

class UpdateAdmin(admin.ModelAdmin):
    fields = ['owner', 'event', 'post_date']

admin.site.register(Psychic, PsychicAdmin)
admin.site.register(Update, UpdateAdmin)
