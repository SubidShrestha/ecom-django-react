from rest_framework import serializers
from .models import *
from customers.serializers import CustomerSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=False,read_only=True,slug_field='title')

    class Meta:
        model = Product
        fields = "__all__"

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many = False,allow_null=False,read_only=True)
    total = serializers.SerializerMethodField(method_name='get_total')
    
    class Meta:
        model = CartItem
        fields = ['product','quantity','total','date_added']
    
    def get_total(self,instance):
        amount = instance.quantity * instance.product.price
        return amount

class CartSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(many=False,read_only=True,slug_field='email')
    items = CartItemSerializer(many=True,read_only=True,allow_null=False)

    cart_total = serializers.SerializerMethodField(method_name='get_cart_total')
    cart_items = serializers.SerializerMethodField(method_name='get_cart_quantity')
    
    class Meta:
        model = Cart
        fields = ['id','customer','items','complete','cart_total','cart_items']

    def get_cart_total(self,instance):
        total = sum([item.total for item in instance.items.all()])
        return total
    
    def get_cart_quantity(self,instance):
        total = sum([item.quantity for item in instance.items.all()])
        return total

class ShippingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False,read_only=True,allow_null=False)
    cart = CartSerializer(many=False,read_only=True,allow_null=False)

    class Meta:
        model = ShippingLocation
        fields = ['id','customer','cart','city','location']
