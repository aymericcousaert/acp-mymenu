from django.contrib import admin

# Register your models here.
from menu.models import Product
from menu.models import PaymentMethod

admin.site.register(Product)
admin.site.register(PaymentMethod)