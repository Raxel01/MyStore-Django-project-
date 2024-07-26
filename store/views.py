from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        allproducts = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(allproducts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        print(serializer.validated_data)
        return Response('This Object is Added')

            

@api_view()
def product_details(request, id):
    pickedProduct = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(pickedProduct)
    return Response(serializer.data)
