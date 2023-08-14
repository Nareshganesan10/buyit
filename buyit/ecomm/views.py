from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from ecomm import serilalizers
from ecomm import models

class UserView(viewsets.ViewSet):

    query_set = models.UserModel.objects.all()

    def list(self, request):
        serilalizer = serilalizers.UserSerializer(self.query_set, many=True)
        return JsonResponse(serilalizer.data, safe=False)        
    
    def create(self, request):
        serilalizer = serilalizers.UserSerializer(data = self.request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return JsonResponse("User account created successfully", safe=False)
        else:
            return JsonResponse(serilalizer.errors, safe=False)
        

class ProductView(viewsets.ViewSet):

    query_set = models.ProductModel.objects.all()

    def list(self, request):
        serilalizer = serilalizers.ProductSerializer(self.query_set, many=True)
        return JsonResponse(serilalizer.data)

    def create(self, request):
        serilalizer = serilalizers.ProductSerializer(data=self.request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return JsonResponse("Succesfully added the product", safe=False)
        else:
            return JsonResponse(serilalizer.errors, safe=False)
    
    def update(self, request, pk=id):
        product = models.ProductModel(pk)
        serilalizer = serilalizers.ProductSerializer(instance=product, data=self.request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=id):
        product = models.ProductModel(pk)
        product.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)
        