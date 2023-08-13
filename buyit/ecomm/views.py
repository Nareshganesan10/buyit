from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
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