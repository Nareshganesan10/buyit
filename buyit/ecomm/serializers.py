from rest_framework import serializers
from ecomm import models

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderModel
        fields = '__all__'

    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = '__all__'