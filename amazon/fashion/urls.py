from django.urls import path
from .import views
urlpatterns=[
    path('fashion1',views.fashion1,name='fashion1'),
     path('fashion2',views.fashion2,name='fashion2')
]