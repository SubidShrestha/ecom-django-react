from django.urls import path
from . import views
from .views import *

urlpatterns = [
    #product
    path('products/',ProductListView.as_view()),
    path('products/get/<str:pk>',ProductDetailsView.as_view()),
    path('products/add',CreateProductView.as_view()),
    path('products/update/<str:pk>',UpdateProductView.as_view()),
    path('products/delete/<str:pk>',DeleteProductView.as_view()),
    #category
    path('category/',CategoryListView.as_view()),
    path('category/get/<str:pk>',CategoryDetailsView.as_view()),
    path('category/add',CreateCategoryView.as_view()),
    path('category/update/<str:pk>',UpdateCategoryView.as_view()),
    path('carts/delete/<str:pk>',DeleteCategoryView.as_view()),
    #cart
    path('carts/',CartListView.as_view()),
    path('carts/get/<str:pk>',CartDetailsView.as_view()),
    path('carts/add',CreateCartView.as_view()),
    path('carts/update/<str:pk>',UpdateCartView.as_view()),
    path('carts/delete/<str:pk>',DeleteCartView.as_view()),
    #cartitem
    path('cartitems/',CartItemsList.as_view()),
    path('cartitems/get/<str:pk>',CartItemDetailsView.as_view()),
    path('cartitems/add',CreateCartItemView.as_view()),
    path('cartitems/update/<str:pk>',UpdateCartItemView.as_view()),
    path('cartitems/delete/<str:pk>',DeleteCartItemView.as_view()),
    #shipping
    path('shipping/',ShippingListView.as_view()),
    path('shipping/get/<str:pk>',ShippingDetailsView.as_view()),
    path('shipping/add',CreateShippingView.as_view()),
    path('shipping/update/<str:pk>',UpdateShippingView.as_view()),
    path('shipping/delete/<str:pk>',DeleteShippingView.as_view()),
]
