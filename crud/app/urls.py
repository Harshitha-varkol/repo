from django.urls import path
from . import views

urlpatterns=[
    path('',views.register,name='create'),
    path('success/<int:user_id>/',views.success,name='success'),
    path('view/<int:user_id>/',views.view_details,name='view'),
    path('edit/<int:user_id>/',views.edit,name='edit'),
]  
