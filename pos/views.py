from ast import Return
from gc import get_objects
from http import HTTPStatus
import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer, ProductShortSerializer
from rest_framework import status
from django.http import Http404
# Create your views here.

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)  
    
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



class ProductsView(APIView):
    permission_classes = (IsAuthenticated,)  

    def get(self, request):
        products = Product.objects.all().order_by('quantity')
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        products_serializer = ProductSerializer(data=request.data)
        if products_serializer.is_valid():
            products_serializer.save()
            print("Zacuva se")
            return Response(status=status.HTTP_201_CREATED, data=products_serializer.data)
        return Response(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product= self.get_object(pk)
        products_serializer = ProductSerializer(product)
        return Response(products_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#class Sale(APIView):
    






@api_view(['GET', 'POST'])
def products_autofill(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('quantity')
        products_serializer = ProductShortSerializer(products, many=True)
        return Response(products_serializer.data, status=status.HTTP_200_OK)
