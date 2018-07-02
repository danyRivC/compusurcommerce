from django.urls import path
from products.views import HomeView, ProductDetailView, ProductSearchView, ProductBuyView
urlpatterns=[
    path('', HomeView.as_view(), name="home"),
    path('search/<query>/', ProductSearchView.as_view(), name="search_product"),
    path('products/<slug:slug>/', ProductDetailView.as_view(),name="detail"),
    path('products/<slug:slug>/buy/', ProductBuyView.as_view(),name="buy")
]