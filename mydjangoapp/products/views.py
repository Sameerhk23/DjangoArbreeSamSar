from django.shortcuts import render, redirect
from .models import Product, CartItem
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms



# Create your views here.
def product_list(request):
    products = Product.objects.all().order_by('quantity')
    return render(request,'products/product_list.html', {'products': products})

def product_details(request,desc='1adas23'):
    return HttpResponse(desc)



@login_required(login_url="/accounts/login/")
def product_create(request):
    if request.method == "POST":
        form= forms.CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            #save product to db
            instance=form.save(commit=False)
            instance.manufacturer=request.user
            instance.save()
            return redirect('products:list')
    else:
        form = forms.CreateProduct()
        return render(request, 'products/product_create.html', {'form': form})
    

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('products:view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('products:view_cart')
