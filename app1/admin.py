# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import OnAppOne
# Register your models here.

class oneAppOneAdmin(admin.ModelAdmin):
    """."""
    list_display = (
        'name',
    )
admin.site.register(OnAppOne, oneAppOneAdmin)
