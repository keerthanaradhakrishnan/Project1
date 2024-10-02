# service_search/urls.py

from django.urls import path
from .views import CategoryListView, SubcategoryListView, ServiceProviderListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('subcategories/', SubcategoryListView.as_view(), name='subcategory-list'),
    path('service-providers/', ServiceProviderListView.as_view(), name='service-provider-list'),
]

