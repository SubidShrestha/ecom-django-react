from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#product api
@api_view(['GET'])
def getProducts(request):
    product_list= Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 3)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filterProducts(request,pk):
    product_list= Product.objects.filter(category = pk)
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 3)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    serializer = ProductSerializer(products,many=True)
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
    cart_list= Cart.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(cart_list, 3)

    try:
        carts = paginator.page(page)
    except PageNotAnInteger:
        carts = paginator.page(1)
    except EmptyPage:
        carts = paginator.page(paginator.num_pages)
    serializer = CartSerializer(carts,many=True)
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
    cartitem_list= CartItem.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(cartitem_list, 3)

    try:
        cartitems = paginator.page(page)
    except PageNotAnInteger:
        cartitems = paginator.page(1)
    except EmptyPage:
        cartitems = paginator.page(paginator.num_pages)
    serializer = CartSerializer(cartitems,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCartItemDetails(request,pk):
    serializer = CartItemSerializer(CartItem.objects.get(id = pk),many=False)
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

#shipping location api
@api_view(['GET'])
def getShippings(request):
    shipping_list= ShippingLocation.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(shipping_list, 3)

    try:
        shippings = paginator.page(page)
    except PageNotAnInteger:
        shippings = paginator.page(1)
    except EmptyPage:
        shippings = paginator.page(paginator.num_pages)
        
    serializer = ShippingSerializer(shippings,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getShippingDetails(request,pk):
    serializer = ShippingSerializer(ShippingLocation.objects.get(id = pk),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addShipping(request):
    serializer = ShippingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateShipping(request,pk):
    Shipping = ShippingLocation.objects.get(id=pk)
    serializer = ShippingSerializer(instance=Shipping,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteShipping(request,pk):
    Shipping = ShippingLocation.objects.get(id=pk)
    serializer = ShippingSerializer(instance=Shipping,data = request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Shipping Item deleted successfully')
