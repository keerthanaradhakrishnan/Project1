from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['profile_image','full_name', 'address', 'date_of_birth', 'gender',
                  'status','house_name', 'landmark', 'pin_code', 'district', 'state']
        read_only_fields = ['custom_id'] 