# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import OnAppTwo


# Register your models here.

class oneAppTwoAdmin(admin.ModelAdmin):
    """."""
    list_display = (
        'name',
    )


admin.site.register(OnAppTwo, oneAppTwoAdmin)
