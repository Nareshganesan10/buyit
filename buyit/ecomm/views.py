from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from ecomm.serializers import ProductSerializer, OrderSerializer, UserSerializer
from ecomm.models import ProductModel, OrderModel, UserModel

class UserView(viewsets.ViewSet):

    query_set = UserModel.objects.all()

    def list(self, request):
        serializers = UserSerializer(self.query_set, many=True)
        return JsonResponse(serializers.data, safe=False)        
    
    def create(self, request):
        serializers = UserSerializer(data = self.request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse("User account created successfully", safe=False)
        else:
            return JsonResponse(serializers.errors, safe=False)
        

class ProductView(viewsets.ViewSet):

    queryset = ProductModel.objects.all()

    def list(self, request):
        serializers = ProductSerializer(self.queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    def create(self, request):
        serializers = ProductSerializer(data=self.request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse("Succesfully added the product", safe=False)
        else:
            return JsonResponse(serializers.errors, safe=False)
    
    def retrieve(self, request, pk):
        products = ProductModel.objects.get(pk=pk)
        serializers = ProductSerializer(data=products)
        return JsonResponse(serializers.data, safe=False)

    
    def update(self, request, pk=None):
        product = ProductModel.objects.get(pk=pk)
        serializers = ProductSerializer(instance=product, data=self.request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=id):
        product = ProductModel(pk)
        product.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)
        