from rest_framework.serializers import ModelSerializer
from products.models import Product,ShortImages
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
        fields = ("id","product_image","product_name","product_price","product_Condition","product_category","product_available","product_sold","product_addittional_fee","product_option","shortImage")
        model = Product
        
    def get_shortImage(self,instance):
        request =  self.context.get("request")
        images = ShortImages.objects.filter(product = instance)
        serializer = ProductShortImageSerializer(images,many=True,context={"request":request})
        return serializer.data
        
        
class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ("id","product_image","product_name","product_price","product_Condition","product_category","product_available","product_sold","product_addittional_fee","product_option","product_section","short_images")
        
    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        
        short_images = self.context.get("request").FILES
        for image in short_images:
            ShortImages.objects.create(short_images=short_images[image],product=product)
            