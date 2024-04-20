from django.contrib import admin
from .models import Cart,CartItem
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "created_by", "status","created_at","updated_at"]


admin.site.register(Cart, CartAdmin)



class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart_id", "product_id", "price","quantity"]

admin.site.register(CartItem, CartItemAdmin)
