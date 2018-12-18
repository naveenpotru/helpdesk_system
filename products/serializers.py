from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User



class ProductSerializer(serializers.ModelSerializer): # create classs to serializer model
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Product
        fields = ('name', 'description', 'manufactue_date', 'created_by')


class UserSerializer(serializers.ModelSerializer): #create class to serealizer usermodel
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'products')