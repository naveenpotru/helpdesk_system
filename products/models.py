from django.db import models

 # Create Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    manufactue_date = models.IntegerField(auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)





