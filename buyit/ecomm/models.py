from django.db import models

class OrderModel(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    delivery_data = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name, self.order_id


class ProductModel(models.Model):
    product_name = models.CharField(max_length=200)
    stock_count = models.IntegerField()

    def __str__(self):
        return self.product_name, self.stock_count


class UserModel(models.Model):
    username =  models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50,)
    is_admin = models.BooleanField()
    is_seller = models.BooleanField()
    # order_id = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=False, unique=True)
    address = models.TextField(null=False)

    def __str__(self):
        return self.username