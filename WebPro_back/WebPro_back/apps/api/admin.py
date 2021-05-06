# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api import models
from django.contrib import admin

# Register your models here.
admin.site.register(models.Comment)
admin.site.register(models.Post)
