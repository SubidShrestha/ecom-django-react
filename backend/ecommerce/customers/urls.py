from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',CustomerListView.as_view()),
    path('get/<str:pk>',CustomerDetailsView.as_view()),
    path('add',CreateCustomerView.as_view()),
    path('update/<str:pk>',UpdateCustomerView.as_view()),
    path('delete/<str:pk>',DeleteCustomerView.as_view()),
]
