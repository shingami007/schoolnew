from django.urls import path
from . import views


urlpatterns=[
    path('home',views.teachers_home),
    path('my-cart',views.view_cart),
    path('my_order',views.view_order)
]  
