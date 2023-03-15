from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("cart/", views.cart, name="cart"),
    path("product-detail/<uuid:uuid>/", views.product_detail, name="product-detail"),
    path("logout/", views.logout, name="logout"),
    path("customer/shop/", views.shop,name="customer-shop"),
    path("customer/register/", views.registration,name="customer-register"),
    path("customer/login/", views.login,name="customer-login"),
    path("choose-login/", views.choose_login,name="choose-login"),
    path("choose-registration/", views.choose_registration,name="choose-registration"),
    
]