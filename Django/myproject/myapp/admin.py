from django.contrib import admin
from .models import MYModel

@admin.register(MYModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'fields2')