

from rest_framework.serializers import ModelSerializer
from products.models import Product, ShortImages, Category, Section
from rest_framework import serializers


class ProductSerializer(ModelSerializer):
    
    product_section = serializers.SerializerMethodField()
    product_category = serializers.SerializerMethodField()
    
    class Meta:
        fields = ("id","product_image","product_name","product_price","product_section","product_category")
        model = Product
        
    def get_product_section(self,obj):
        return obj.product_section.section_name
    
    def get_product_category(self,obj):
        return obj.product_category.category_name
    
    
class ProductShortImageSerializer(ModelSerializer):
    class Meta:
        fields = ("id","short_images")
        model = ShortImages
    

class ProductDetailSerializer(ModelSerializer):
    
    shortImage = serializers.SerializerMethodField()
    
    class Meta:
        fields = ("id","product_image","product_name","product_price","product_Condition","product_category","product_available","product_sold","product_addittional_fee","product_option","shortImage","product_featured")
        model = Product
        
    def get_shortImage(self,instance):
        request =  self.context.get("request")
        images = ShortImages.objects.filter(product = instance)
        serializer = ProductShortImageSerializer(images,many=True,context={"request":request})
        return serializer.data
        



class ProductCreateSerializer(serializers.ModelSerializer):
    short_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    product_category = serializers.CharField()
    product_section = serializers.CharField()

    class Meta:
        model = Product
        fields = (
            "product_image", "product_name", "product_price", 
            "product_description", "product_featured", "product_Condition", 
            "product_available", "product_sold", "product_option", 
            "product_addittional_fee", "product_category", "product_section", 
            "short_images"
        )

    def create(self, validated_data):
        short_images_data = validated_data.pop('short_images', [])
        category_name = validated_data.pop('product_category')
        section_name = validated_data.pop('product_section')
        
        category = Category.objects.get_or_create(category_name=category_name)[0]
        section = Section.objects.get_or_create(section_name=section_name)[0]
        
        product = Product.objects.create(
            product_category=category, 
            product_section=section, 
            **validated_data
        )

        for image_data in short_images_data:
            ShortImages.objects.create(product=product, short_images=image_data)

        return product