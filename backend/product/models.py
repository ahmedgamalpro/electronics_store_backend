from django.db import models

DISCOUNT = [
    ("NONE","none"),
    ("PERCENT","percent"),
    ("AMOUNT","amount"),
]

#Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category_id =models.ForeignKey( Category,on_delete=models.CASCADE)
    title = models.CharField( max_length=250)
    picture =models.CharField( max_length=250)
    summary = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    discount_type = models.CharField(max_length=50, choices=DISCOUNT,default='none')
    discount_value = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
    def __str__(self):
        return f"{self.title}"
class Review(models.Model):
    id = models.AutoField(primary_key=True)





