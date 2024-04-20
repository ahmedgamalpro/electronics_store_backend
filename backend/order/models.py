from django.db import models
from user.models import User
from product.models import Product

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderLine(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, verbose_name=("Product"), on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, verbose_name=("Product"), on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()