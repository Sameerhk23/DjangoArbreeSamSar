from django.shortcuts import render, redirect
from .models import Product
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