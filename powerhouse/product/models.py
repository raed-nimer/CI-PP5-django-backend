from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

# Category model
class Category(models.Model):
    name = models.CharField(max_length=200)  # required
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
# Product model
class Product(models.Model):
    name = models.CharField(max_length=200)  # required
    description = models.TextField()  # required
    price = models.DecimalField(max_digits=10, decimal_places=2)  # required
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # required
    image = CloudinaryField('image')
    #image = models.ImageField(upload_to='products/', blank=True, null=True, default='products/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)