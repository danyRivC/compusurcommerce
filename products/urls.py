from django.urls import path
from products.views import HomeView, ProductDetailView, ProductBuyView, search_product, ProductByCategory
urlpatterns=[
    path('', HomeView.as_view(), name="home"),
    path('products/categories/<query>', ProductByCategory.as_view(), name="product_category" ),
    path('search/',search_product , name="search_product"),
    path('products/<slug:slug>/', ProductDetailView.as_view(),name="detail"),
    path('products/<slug:slug>/buy/', ProductBuyView.as_view(),name="buy")
]
