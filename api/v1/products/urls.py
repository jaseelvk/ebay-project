from django.urls import path
from . import views

urlpatterns = [
    path('', views.products),
    path('view/<int:pk>', views.product),
    path('create/', views.create_product), 
]
