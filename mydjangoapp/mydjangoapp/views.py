from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage')
    return render(request,'homepage.html')
def product(request):
    # return HttpResponse('product')
    return render(request,'product.html')
def user(request):
    # return HttpResponse('user')
    return render(request,'user.html')
def blog(request):
    # return HttpResponse('blog')
    return render(request,'blog.html')