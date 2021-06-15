
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.productList, name='product-list'),
    path('<slug:category_slug>/', views.productList, name='product-list-category'),
    path('detail/<slug:product_slug>/', views.productDetail, name='product-detail'),
]
