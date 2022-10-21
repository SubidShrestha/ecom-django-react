from django.contrib import admin
from .models import *

class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('id','customer','date_ordered','cart_total','cart_items')

class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ('id','product','cart','quantity','date_added','total')

class ShippingAdmin(admin.ModelAdmin):
    model = ShippingLocation
    list_display = ('id' ,'cart','address')

admin.site.register(Product)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,CartItemAdmin)
admin.site.register(ShippingLocation,ShippingAdmin)
