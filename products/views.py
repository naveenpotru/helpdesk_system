from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET', 'DELETE', 'PUT']) # Methods Allowed
@permission_classes((IsAuthenticated, IsOwnerOrReadOnly,)) # Pemissions, Only Authenticated user
def get_delete_update_product(request, pk):  #pk es PrimaryKey(Id)
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        content = {
            'status': 'Not Found'
        }
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    # details a sinlge product
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    # delete a product
    elif request.method == 'DELETE':
        if(request.user == product.created_by): # If created_by is who makes request
            product.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
    # update a product
    elif request.method == 'PUT':
        if(request.user == product.created_by): # If created_by is who makes request
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def get_post_products(request):
    # get all products
    if request.method == 'GET':
        puppies = Product.objects.all()
        serializer = ProductSerializer(puppies, many=True)
        return Response(serializer.data)

    # create a new product
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

