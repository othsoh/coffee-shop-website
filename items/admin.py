from django.contrib import admin
from .models import Product,Cart,CartItem

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "is_available", "categorie"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
