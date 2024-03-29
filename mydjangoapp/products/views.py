from django.shortcuts import render, redirect
from .models import Product, CartItem
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
from django.contrib import messages
from .forms import CheckoutForm



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
    total_price = sum(item.product.price * item.quantity - item.discount for item in cart_items)
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


def apply_discount(request):
    if request.method == 'POST':
        discount_amount = request.POST.get('discount', 0)
        try:
            discount_amount = float(discount_amount)
        except ValueError:
            messages.error(request, 'Invalid discount amount. Please enter a valid number.')
            return redirect('products:view_cart')

        # Apply the discount to each cart item
        cart_items = CartItem.objects.all()
        for item in cart_items:
            item.discount = discount_amount
            item.save()

        messages.success(request, f'Discount of ${discount_amount} applied to your cart.')
        return redirect('products:view_cart')
    else:
        return redirect('products:view_cart')
    

#function for checkout
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Your payment processing logic goes here
            payment_method = form.cleaned_data['payment_method']

            if payment_method == 'cash':
                # If payment is by cash, redirect to the success page
                CartItem.objects.filter(user=request.user).delete()
                return render(request, 'checkout_success.html')

            # Continue processing for other payment methods...
            # For a real application, you would integrate with a payment gateway

    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'cart_items': cart_items, 'form': form})