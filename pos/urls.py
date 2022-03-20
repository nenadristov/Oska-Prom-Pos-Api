from os import name
from django.urls import path
from pos import views
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='productDetai'),
    path('products-listing/', views.products_autofill, name='products-for-listing-and-autofill'),
]