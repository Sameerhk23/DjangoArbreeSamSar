
from django.urls import path
from .import views

app_name='products'

urlpatterns = [
    
    
    

    path('',views.product_list,name="list"),
    path('create/', views.product_create, name ="create"),

    path('desc/<desc>',views.product_details,name="detail"),
    path('desc',views.product_details,name="detail"),
    path('products/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

]