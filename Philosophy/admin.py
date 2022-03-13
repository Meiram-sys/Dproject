from django.contrib import admin

from .models import *


class PhilosophyModel(admin.ModelAdmin):
    class Meta:
        name = philosophers


class IdeaModel(admin.ModelAdmin):
    class Meta:
        name = philosophy_ideas


admin.site.register(philosophers, PhilosophyModel)
admin.site.register(philosophy_ideas, IdeaModel)
