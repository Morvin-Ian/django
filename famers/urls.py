from django.urls import path
from . import views

urlpatterns = [
    path("<uuid:uuid>/", views.index, name='farmer-index'),
    path("register/", views.registration,name="farmer-register"),
    path("login/", views.login,name="farmer-login"), 
    path("post-product/<uuid:uuid>/", views.post_product, name='post-product'),
    path("edit-product/<uuid:uuid>/", views.edit_product, name='edit-product'),
    path("delete-product/<uuid:uuid>/", views.delete_product, name='delete-product'),
    path("subsidized_product/<uuid:uuid>/", views.subsidized_products, name='subsidized-product'),
    path("subsidized_detail/<uuid:uuid>/", views.subsidized_detail, name='subsidized_detail'),
    path("your-products/<uuid:uuid>/", views.farmer_products, name='farmer_products'),

   
]