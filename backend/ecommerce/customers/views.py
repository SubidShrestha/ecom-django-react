from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomerListView(ListAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    pagination_class=PageNumberPagination
        
class CustomerDetailsView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CreateCustomerView(GenericAPIView):
    serializer_class= RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        
class UpdateCustomerView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class=CustomerSerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)

class DeleteCustomerView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)