from django.db import models


ROLE = [
    ("CUSTOMER","customer"),
    ("ADMIN","admin"),
]
# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField()
    email = models.EmailField(max_length=254,unique=True)
    # password = models.CharField(max_length=50)
    role = models.CharField(choices=ROLE, max_length=50)
    avatar = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.email
