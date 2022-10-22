from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.getProducts),
    path('products/filter/<str:pk>',views.filterProducts),
    path('products/<str:pk>',views.getProductDetails),
    path('products/add',views.addProduct),
    path('products/update/<str:pk>',views.updateProduct),
    path('products/delete/<str:pk>',views.deleteProduct),
    path('category/',views.getCategory),
    path('category/<str:pk>',views.getCategoryDetails),
    path('category/add',views.addCategory),
    path('category/update/<str:pk>',views.updateCategory),
    path('carts/delete<str:pk>',views.deleteCategory),
    path('carts/',views.getCarts),
    path('carts/<str:pk>',views.getCartDetails),
    path('carts/add',views.addCart),
    path('carts/update/<str:pk>',views.updateCart),
    path('carts/delete<str:pk>',views.deleteCart),
    path('cartitems/',views.getCartItems),
    path('cartitems/<str:pk>',views.getCartItemDetails),
    path('cartitems/add',views.addCartItem),
    path('cartitems/update/<str:pk>',views.updateCartItem),
    path('cartitems/delete<str:pk>',views.deleteCartItem),
]
