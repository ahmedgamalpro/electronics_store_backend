from django.contrib import admin
from .models import Product, Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","category_id","title","price"]

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Category, CategoryAdmin)