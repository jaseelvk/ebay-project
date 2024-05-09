from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product,Category, Section ,ShortImages
from .serializers import ProductSerializer,ProductDetailSerializer,ProductCreateSerializer

@api_view(['GET'])
def products(request):
    instances = Product.objects.filter(product_available__gt=0) 
    context = {
        "request":request
            
    }
    serializer = ProductSerializer(instances,many=True,context=context)
    response_data = {
        "status_code": 6000,
        "data": serializer.data,
    }
    
    return Response(response_data)



@api_view(['GET'])
def product(request, pk):  
    if Product.objects.filter(pk=pk).exists():
        instance = Product.objects.get(pk=pk) 
        context = {
            "request": request
        }
        serializer = ProductDetailSerializer(instance, context=context)
        response_data = {
            "status_code": 6000,
            "data": serializer.data,
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "Product does not exist",
        }
        return Response(response_data)




@api_view(['POST'])
def create_product(request):
    serializer = ProductCreateSerializer(data=request.data)
    if serializer.is_valid():
        # Extract category and section data from the request
        category_id = request.data.get('product_category')
        section_id = request.data.get('product_section')
        
        # Retrieve category and section objects
        category = get_object_or_404(Category, pk=category_id)
        section = get_object_or_404(Section, pk=section_id)
        
        # Add category and section to the validated data
        serializer.validated_data['product_category'] = category
        serializer.validated_data['product_section'] = section
        
        # Save the product
        serializer.save()
        
        response_data = {
            "status_code": 6000,
            "message": "Product created successfully",
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "Product creation failed",
            "data": serializer.errors,
        }
        
    return Response(response_data)