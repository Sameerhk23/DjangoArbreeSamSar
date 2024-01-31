
from django.urls import path
from .import views

app_name='products'

urlpatterns = [
    
    
    

    path('',views.product_list,name="list"),
    path('create/', views.product_create, name ="create"),

    path('desc/<desc>',views.product_details,name="detail"),
    path('desc',views.product_details,name="detail"),
]