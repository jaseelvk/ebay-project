from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
    
class Section(models.Model):
    section_name = models.CharField(max_length=100)
   

    class Meta:
        verbose_name_plural = 'sections'

    def __str__(self):
        return self.section_name
    
    
class Product(models.Model):
    product_image = models.ImageField(upload_to='images/')
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_featured = models.BooleanField(default=False)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_Condition = models.CharField(max_length=100)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    product_available = models.IntegerField()
    product_sold = models.IntegerField()
    product_option = models.CharField(max_length=100)
    product_addittional_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.product_name
    
    

    

class ShortImages (models.Model):
    short_images = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='short_images')




class WishList (models.Model):
    product_wishlist = models.ForeignKey(Product, on_delete=models.CASCADE)
