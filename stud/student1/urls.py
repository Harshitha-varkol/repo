from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('index',views.index,name='py'),
    path('index1',views.index1,name='j'),
    path('index2',views.index2,name='q'),
]

