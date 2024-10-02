from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.permissions import AllowAny

# Create a new customer profile (POST)
class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]
    # permission_classes = [permissions.IsAuthenticated]

# List all customer profiles (GET)
class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]
    # permission_classes = [permissions.IsAuthenticated]

# Retrieve, Update (PUT or PATCH) and Delete (DELETE) a specific customer profile (GET, PUT, PATCH, DELETE)
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]
