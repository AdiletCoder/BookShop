from django.urls import path

from .views import create_order

urlpatterns = [
    path('create/<int:book_id>', create_order, name='create-order'),

]














