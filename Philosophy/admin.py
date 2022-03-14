from django.contrib import admin

from .models import *


class PhilosophyModel(admin.ModelAdmin):
    class Meta:
        name = philosophers

class IndividualModel(admin.ModelAdmin):
    class Meta:
        name = Individuals

class CategoryModel(admin.ModelAdmin):
    class Meta:
        name = category


admin.site.register(philosophers, PhilosophyModel)
admin.site.register(Individuals,IndividualModel)
admin.site.register(category,CategoryModel)