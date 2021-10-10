from django.contrib import admin
from .models import *


class AdminManager(admin.ModelAdmin):
    list_display = ['id', 'segment', 'country', 'units', 'sales', 'datesold']



admin.site.register(Product, AdminManager)