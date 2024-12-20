from django.shortcuts import render, redirect, get_object_or_404

from .models import Product

def home(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()
    ctx = {'products': products}
    return render(request, 'products/product-list.html', ctx)

def product_create(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        if product_name and description and price and image and category:
            Product.objects.create(
            product_name=product_name,
            description=description,
            price=price,
            image=image,
            category=category,
        )
        return redirect('products:list')
    return render(request, 'products/product-create.html')

def about(request):
    return render(request, 'products/about.html')

def product_category(request, category):
    products = Product.objects.filter(category=category)
    ctx = {'products': products}
    return render(request, 'products/product-list.html', ctx)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    ctx = {'product': product}
    return render(request, 'products/product-detail.html', ctx)


