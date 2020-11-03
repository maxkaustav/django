from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('profile',views.profile),
    path('customer/',views.customer),
    path('products',views.products)
]