from email.policy import default
from django.db import models
from customers.models import Customer

class Product(models.Model):
    name=models.CharField(max_length=60,null=False)
    image=models.ImageField(upload_to='products/',null=False)
    CATEGORIES =[('Mens Wear','Mens Wear'),
                ('Womens Wear','Womens Wear'),
                ('Accessories','Accessories'),
                ('Electronics','Electronics')
                ]
    category=models.CharField(max_length=60,choices = CATEGORIES,null=False)
    price=models.IntegerField(default=0)
    description=models.TextField(max_length=255,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,related_name='buyer')
    date_ordered = models.DateField(auto_now_add = True)
    complete = models.BooleanField(default=False)

    @property
    def cart_total(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.total for item in cartitems])
        return total
    
    @property
    def cart_items(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.quantity for item in cartitems])
        return total
    
    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=False,related_name='items')
    quantity = models.IntegerField(default = 0)
    date_added = models.DateField(auto_now_add=True)

    @property
    def total(self):
        amount = self.product.price * self.quantity
        return amount

class ShippingLocation(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=False)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=False)
    city = models.CharField(max_length=40,null=False)
    location = models.CharField(max_length=40,null=False)

    @property
    def address(self):
        loc = self.location + ", " + self.city
        return loc
    
    def __str__(self):
        return self.address