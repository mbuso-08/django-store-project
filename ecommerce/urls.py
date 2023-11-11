from django.urls import path
from .views import HomeView, ItemDetailView, add_to_cart, show_cart, remove_from_cart
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='show-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove_from_cart'),
]