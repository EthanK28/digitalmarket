from django.contrib import admin

# Register your models here.
from .models import Product, Thumbnail


class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id", "description", "price", "sale_price"]
    search_fields = ["title", "description"]
    list_filter = ["price"]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

admin.site.register(Thumbnail)


