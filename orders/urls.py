from django.urls import path
from .views import checkout

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
]
from django.urls import path
from .views import checkout, create_admin

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('create-admin/', create_admin, name='create_admin'),
]