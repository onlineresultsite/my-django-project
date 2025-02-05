from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path("cart/item/<str:u_id>", views.cart_view, name="cart_view" ),
    path("product/item/<str:uid>", views.view_product, name="view_product" ),
    path("products/", views.products, name="products" ),
    path("cart/", views.cart, name="cart" ),
    path("cart-item-delete/<str:puid>/", views.delete_cart_product, name="delete_cart_product" ),
    path("item-include/<str:the_id>/", views.cart_plus, name="cart_plus" ),
    path("item-remove/<str:the_id>/", views.cart_minus, name="cart_minus" ),
]
