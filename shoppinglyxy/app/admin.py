from django.contrib import admin
from .models import (
    Cart,
    OrderPlaced,
    Product,
    Customer
)
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
 list_dispaly = ['id', 'user', 'name','locality','city','zipcode','state']

@admin.register(Product)
class CustomerModelAdmin(admin.ModelAdmin):
 list_dispaly = ['id', 'title', 'selling_price','discounted_price','description','brand','category','product_image'] 

@admin.register(Cart)
class CustomerModelAdmin(admin.ModelAdmin):
 list_dispaly = ['id', 'user' , 'product' , 'quantity']

@admin.register(OrderPlaced)
class CustomerModelAdmin(admin.ModelAdmin):
 list_dispaly = ['id', 'user', 'customer','product','quantity','order_date','status']
