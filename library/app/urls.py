from django.urls import path
from . import views

urlpatterns=[
    path("",views.library,name="home"),
    path("list/",views.list,name="display_books"),
    path('show/',views.show,name="show"),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('success',views.success,name='success')
]