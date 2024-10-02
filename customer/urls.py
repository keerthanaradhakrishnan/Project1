from django.urls import path
from .views import CustomerCreateView, CustomerListView, CustomerDetailView

urlpatterns = [
    path('api/customer/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('api/customer/list/', CustomerListView.as_view(), name='customer-list'),
    path('api/customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
]



