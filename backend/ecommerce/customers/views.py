from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@api_view(['GET'])
def getCustomer(request):
    customer_list= Customer.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(customer_list, 3)

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)
        
    serializer = CustomerSerializer(customers,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCustomerDetails(request,pk):
    serializer = CustomerSerializer(Customer.objects.get(id = pk),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addCustomer(request):
    serializer = CustomerSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer,data = request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Customer deleted successfully')