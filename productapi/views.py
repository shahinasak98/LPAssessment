from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductView(APIView):

    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response({"Result":serializer.data},status=status.HTTP_201_CREATED)

    def post(self,request):
        data=request.data
        serializer=ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        product=serializer.save()
        return Response({"Result":"Product added successfully"},status=status.HTTP_201_CREATED)

class ProductIDView(APIView):
    def get(self,request,pk):
        try:
            product=Product.objects.get(id=pk)
            serializer=ProductSerializer(product)
            return Response({'Result':serializer.data},status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({"Result":"Sorry! Product with this ID doesnot exist"},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            product=Product.objects.get(id=pk)
            serializer=ProductSerializer(product,data=request.data)
            serializer.is_valid(raise_exception=True)
            product=serializer.save()
            return Response({"Result":[serializer.data,"Updated Succesfully"]},status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({"Result":"Sorry! Product with this ID doesnot exist"},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            product=Product.objects.get(id=pk)
            product.delete()
            return Response({"Result":"Product deleted successfully"})
        except Product.DoesNotExist:
            return Response({"Result":"Sorry! Product with this ID doesnot exist"},status=status.HTTP_400_BAD_REQUEST)


