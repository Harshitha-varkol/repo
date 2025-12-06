from django.urls import path
from .import views

urlpatterns=[
    path('',views.mxplayer1,name='mxplayer1'),
    path('',views.mxplayer2,name='mxplayer2'),
]