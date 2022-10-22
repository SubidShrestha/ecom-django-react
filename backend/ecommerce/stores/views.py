from .serializers import ProductSerializer, CartSerializer,CartItemSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *

#product api
@api_view(['GET'])
def getProducts(request):
    serializer = ProductSerializer(Product.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filterProducts(request,pk):
    serializer = ProductSerializer(Product.objects.filter(category = pk),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductDetails(request,pk):
    serializer = ProductSerializer(Product.objects.get(id = pk),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product,data = request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Product deleted successfully')

#category api
@api_view(['GET'])
def getCategory(request):
    serializer = CategorySerializer(Category.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategoryDetails(request,pk):
    serializer = CategorySerializer(Category.objects.get(id = pk),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addCategory(request):
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateCategory(request,pk):
    cart = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=cart,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCategory(request,pk):
    cart = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=cart,data = request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Category deleted successfully')

#cart api
@api_view(['GET'])
def getCarts(request):
    serializer = CartSerializer(Cart.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCartDetails(request,pk):
    serializer = CartSerializer(Cart.objects.get(id = pk),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addCart(request):
    serializer = CartSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateCart(request,pk):
    cart = Cart.objects.get(id=pk)
    serializer = CartSerializer(instance=cart,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCart(request,pk):
    cart = Cart.objects.get(id=pk)
    serializer = CartSerializer(instance=cart,data = request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Cart deleted successfully')

#cart items api
@api_view(['GET'])
def getCartItems(request):
    serializer = CartItemSerializer(CartItem.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCartItemDetails(request,pk):
    serializer = CartSerializer(CartItem.objects.get(id = pk),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addCartItem(request):
    serializer = CartItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateCartItem(request,pk):
    cartitem = CartItem.objects.get(id=pk)
    serializer = CartItemSerializer(instance=cartitem,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCartItem(request,pk):
    cartitem = CartItem.objects.get(id=pk)
    serializer = CartItemSerializer(instance=cartitem,data = request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Cart Item deleted successfully')