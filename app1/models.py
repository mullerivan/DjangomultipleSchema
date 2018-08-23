from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from app2.models import OnAppTwo

# Create your models here.
@python_2_unicode_compatible
class OnAppOne(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True,
        blank=False,
        null=False
    )
    two = user = models.ForeignKey(OnAppTwo,
                                   blank=True,
                                   null=True)

    user = models.ForeignKey(User,
                             blank=True,
                             null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'"app1\".\"on_app_one"'
