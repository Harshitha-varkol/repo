from django.urls import path
from . import views

urlpatterns=[
    path('dresses',views.dresses),

    path('tops',views.tops),

    path('shrugs',views.shrugs),

    path('sarees',views.sarees),

    path('tshirt',views.tshirt),

    path('lehanga',views.lehanga),

    path('jeans',views.jeans),

    path('dupatta',views.dupatta),

    path('jumpsuits',views.jumpsuits),

    path('kurtas',views.kurtas),

    path('material',views.material),

    path('playsuits',views.playsuits),

    path('jackets',views.jackets),

    path('skirts',views.skirts),
    
    path('coords',views.coords),
    
    path('flats',views.flats),

    path('dress',views.dress),

    path('clothing',views.clothing),

    path('footwear',views.footwear),

    path('spacc',views.sportsacc),

    path('spequi',views.sportsequi), 

    path('boots',views.boots), 

    path('shoes',views.casualshoes), 

    path('earrings',views.earrings), 

    path('jewellery',views.fashionjewellery), 

    path('jewel',views.finejewellery), 

    path('gadjets',views.fitnessgadjets),

    # path('flats',views.flats), 

    path('headphones',views.headphones), 

    path('smart',views.smartwearables), 

    path('speakers',views.speakers), 

    path('sportshoe',views.sportshoe), 

    path('heels',views.heels),

    path('dresses',views.dresses)
]