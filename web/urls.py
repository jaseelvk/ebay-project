from django.urls import path
from products.views import product
from web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:id>/", product, name='product'),
    path('add-wishlist/', views.add_wishlist, name='add_wishlist'),
    path('remove-wishlist/', views.remove_wishlist, name='remove_wishlist'),
    path('my-wishlist/', views.my_wishlist, name='my_wishlist'),
]
