from .serializers import *
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.pagination import PageNumberPagination

#product api
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]

    filterset_fields=['category','price']
    search_fields=['id','name']
    ordering_fields=['id','name','price']
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateProductView(CreateAPIView):
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

    def perform_update(self, serializer):
        return super().perform_create(serializer)

class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

    def perform_destroy(self, serializer):
        return super().perform_destroy(serializer)

#category api
class CategoryListView(ListAPIView):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer
    pagination_class=PageNumberPagination

class CreateCategoryView(CreateAPIView):
    serializer_class=CategorySerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class CategoryDetailsView(RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class UpdateCategoryView(UpdateAPIView):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)

class DeleteCategoryView(DestroyAPIView):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer

    def perform_destroy(self, serializer):
        return super().perform_destroy(serializer)

#cart api
class CartListView(ListAPIView):
    queryset= Cart.objects.all()
    serializer_class=CartSerializer
    pagination_class=PageNumberPagination

class CreateCartView(CreateAPIView):
    serializer_class=CartSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class CartDetailsView(RetrieveAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class UpdateCartView(UpdateAPIView):
    queryset= Cart.objects.all()
    serializer_class=CartSerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)

class DeleteCartView(DestroyAPIView):
    queryset= Cart.objects.all()
    serializer_class=CartSerializer

    def perform_destroy(self, serializer):
        return super().perform_destroy(serializer)

#cart items api
class CartItemsList(ListAPIView):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer
    pagination_class=PageNumberPagination

class CreateCartItemView(CreateAPIView):
    serializer_class=CartItemSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class CartItemDetailsView(RetrieveAPIView):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer

class UpdateCartItemView(UpdateAPIView):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)

class DeleteCartItemView(DestroyAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartItemSerializer

    def perform_destroy(self, serializer):
        return super().perform_destroy(serializer)

#shipping location api
class ShippingListView(ListAPIView):
    queryset=ShippingLocation.objects.all()
    serializer_class=ShippingSerializer
    pagination_class=PageNumberPagination

class CreateShippingView(CreateAPIView):
    serializer_class=ShippingSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class ShippingDetailsView(RetrieveAPIView):
    queryset=ShippingLocation.objects.all()
    serializer_class=ShippingSerializer

class UpdateShippingView(UpdateAPIView):
    queryset=ShippingLocation.objects.all()
    serializer_class=ShippingSerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)

class DeleteShippingView(DestroyAPIView):
    queryset=ShippingLocation.objects.all()
    serializer_class=ShippingSerializer

    def perform_destroy(self, serializer):
        return super().perform_destroy(serializer)
