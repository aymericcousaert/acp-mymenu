from django.contrib import admin

# Register your models here.

from menu.models import Product
from menu.models import PaymentMethod
from menu.models import Category
from menu.models import DailySpecial
from menu.models import Promotion

admin.site.register(Product)
admin.site.register(PaymentMethod)
admin.site.register(Category)
admin.site.register(DailySpecial)
admin.site.register(Promotion)

