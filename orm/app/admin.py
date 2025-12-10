from django.contrib import admin
from .models import Library
@admin.register(Library)
# Register your models here.

class LibraryAdmin(admin.ModelAdmin):
    list_display=['name','author']

