from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True)  # No unique slug field
    description = models.TextField(default='No description provided')
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    description = models.TextField(default='No description provided')
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')

    def __str__(self):
        return self.title


class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    #subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='service_providers')
    description = models.TextField()
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')

    def __str__(self):
        return self.name

