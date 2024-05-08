import json
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from products.models import Category, Product, Section, WishList


def index(request):
    categories = Category.objects.all()
    sections = Section.objects.all()
    category_id = request.GET.get('category_id')

    # Filter Items by category
    filter_category = request.GET.get('options')

    if filter_category and filter_category != 'All':
        products = Product.objects.filter(product_category__category_name=filter_category)
        sections = Section.objects.filter(product__product_category__category_name=filter_category).distinct()
    elif filter_category == 'All':
        return redirect('web:index')
    else:
        products = Product.objects.all()

    if category_id:
        products = products.filter(product_section__category__id=category_id)
   
    # Filter only featured products
    featured_products = products.filter(product_featured=True)
   
    # search items by product name and price
    query = request.GET.get('query', '')
    if query:
        products = products.filter(
            Q(product_name__icontains=query) |
            Q(product_price__icontains=query)
        )
        sections = Section.objects.filter(product__in=products).distinct()
        
      # Check if products are in wishlist
    wishlist_products = WishList.objects.filter(product_wishlist__in=products).values_list('product_wishlist__id', flat=True)
    context ={
        "title" : "Home Page",
        "categories": categories,
        "category_id": category_id,
        "products": products,
        "sections": sections,
        "selected_category": filter_category,
        "featured_products": featured_products,
        "wishlist_products": wishlist_products,  
        "query": query, 
    }
    return render(request, 'web/index.html', context=context)


def add_wishlist(request):
    pid = request.GET.get('product')  
    if pid:
        try:
            product = Product.objects.get(id=pid)
            # Add product to wishlist
            wishlist, created = WishList.objects.get_or_create(product_wishlist=product)
            if created:
                return JsonResponse({'bool': True})
            else:
                return JsonResponse({'bool': False, 'error': 'Product already in wishlist'})
        except Product.DoesNotExist:
            return JsonResponse({'bool': False, 'error': 'Product does not exist'}, status=404)
    else:
        return JsonResponse({'bool': False, 'error': 'Invalid request'}, status=400)

def remove_wishlist(request):
    pid = request.GET.get('product')  
    if pid:
        try:
            product = Product.objects.get(id=pid)
            # Remove product from wishlist
            deleted_count, _ = WishList.objects.filter(product_wishlist=product).delete()
            if deleted_count > 0:
                return JsonResponse({'bool': True})
            else:
                return JsonResponse({'bool': False, 'error': 'Product is not in the wishlist'})
        except Product.DoesNotExist:
            return JsonResponse({'bool': False, 'error': 'Product does not exist'}, status=404)
    else:
        return JsonResponse({'bool': False, 'error': 'Invalid request'}, status=400)


def my_wishlist(request):
    my_wishlist_products = WishList.objects.select_related('product_wishlist').order_by('-id')
    return render(request, 'web/wishlist.html', {'wishlist': my_wishlist_products})
