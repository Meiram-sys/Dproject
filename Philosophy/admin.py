from django.contrib import admin

from .models import *


class PhilosophyModel(admin.ModelAdmin):
    class Meta:
        name = philosophers



admin.site.register(philosophers, PhilosophyModel)

