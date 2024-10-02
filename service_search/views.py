from rest_framework import generics
from django.db.models import Q  # Import Q for filtering
from .models import Category, Subcategory, ServiceProvider
from .serializers import CategorySerializer, SubcategorySerializer, ServiceProviderSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('search', None)  # Get search query

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))  # Search by title or description
        
        return queryset


class SubcategoryListView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('search', None)  # Get search query

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        
        return queryset


class ServiceProviderListView(generics.ListAPIView):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('search', None)  # Get search query

        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
        
        return queryset


