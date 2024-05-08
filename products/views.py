from django.shortcuts import render,get_object_or_404

from .models import Product


def product(request, id):
    instance = get_object_or_404(Product, id=id)
    related_items = Product.objects.filter(product_section=instance.product_section).exclude(id=instance.id)[:5]
    
    context = {
        'instance': instance,
        'related_items': related_items
    }
    return render(request, 'web/single.html', context=context)
