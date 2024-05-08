from django.contrib import admin

from .models import Category, Product, Section, ShortImages,WishList

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name')
    ordering = ('id','category_name')

class ShortImageAdmin(admin.TabularInline):
    model = ShortImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ShortImageAdmin]
    list_display = ('id','product_name')
    ordering = ('id','product_name')




admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Section)
admin.site.register(WishList)
