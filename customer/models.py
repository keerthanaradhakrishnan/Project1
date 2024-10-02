# from django.contrib.auth.models import User,Permission,Group
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import re
import random
import string

from .validators import validate_file_size

class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    #custom_id = models.CharField(max_length=20, unique=True, editable=False, blank=True)  # Custom ID field
    profile_image = models.ImageField(upload_to='c-profile-images/', null=True, blank=True, validators=[validate_file_size])#Customer specific field
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    date_of_birth = models.DateField()#Customer specific field
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)#Customer specific field
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])#Customer specific field
    house_name = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.custom_id:
            # Find the last existing custom ID
            last_custom_id = Customer.objects.order_by('custom_id').last()
            if last_custom_id:
                 # Extract the numeric part and increment
                match = re.match(r'USER(\d+)', last_custom_id.custom_id)
                if match:
                    customer_number = int(match.group(1)) + 1
                else:
                    customer_number = 1 # Start from 1 if no previous ID found
            else:
                customer_number = 1 # Start from 1 if no previous ID found

            # Create the custom ID with the USER prefix
            self.custom_id = f'USER{customer_number}'  # No leading zeros

        super(Customer, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.custom_id



   

