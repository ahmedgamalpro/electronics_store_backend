from django.db import models
from user.models import User
from product.models import Product

CARTSTATUS = [
    ("ORDERED","ordered"),
    ("ADANDONNED","abandonned"),
]

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    status = models.CharField( choices=CARTSTATUS,max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, verbose_name=("Product"), on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, verbose_name=("Product"), on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()