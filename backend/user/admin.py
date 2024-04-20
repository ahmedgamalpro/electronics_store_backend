from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "slug", "email","role","avatar","created_at","updated_at"]


admin.site.register(User, UserAdmin)