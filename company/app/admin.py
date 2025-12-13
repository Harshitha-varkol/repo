from django.contrib import admin

from .models import(Employeetable)
@admin.register(Employeetable)
class EmpAdmin(admin.modelAdmin):
    list_display=['name','phone']
    list_display_links=['name','phone']
    