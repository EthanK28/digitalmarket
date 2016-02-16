from django.contrib import admin

# Register your models here.
from .models import (
    Product, Thumbnail,
    MyProducts
)

class ThumbnailInline(admin.TabularInline):
    extra = 1

    model = Thumbnail



class ProductAdmin(admin.ModelAdmin):
    inlines = [ThumbnailInline]
    list_display = ["__str__", "id", "description", "price", "sale_price"]
    search_fields = ["title", "description"]
    list_filter = ["price"]
    prepopulated_fields = {"slug": ("title", )}
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(MyProducts)


