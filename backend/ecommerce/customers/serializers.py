from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','email','password','first_name','last_name','gender','city','location']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('email','password','first_name','last_name','gender','city','location')
    
    def create(self,validated_data):
        return Customer.objects.create_user(**validated_data)
    
    