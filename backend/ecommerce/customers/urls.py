from django.urls import path
from . import views

urlpatterns = [
    path('',views.getCustomer),
    path('<str:pk>',views.getCustomerDetails),
    path('add',views.addCustomer),
    path('update/<str:pk>',views.updateCustomer),
    path('delete<str:pk>',views.deleteCustomer),
]
