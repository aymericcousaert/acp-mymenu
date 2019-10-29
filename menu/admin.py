from django.contrib import admin

# Register your models here.

from menu.models import Product
from menu.models import PaymentMethod
from menu.models import Category
from menu.models import DailySpecial
from menu.models import Promotion
from menu.models import Client


class ClientAdmin(admin.ModelAdmin):
    actions = ['send_email']

    def send_email(self, request, queryset):
        # complete this function
        a = 10

    send_email.short_description = "Send email to selected clients with suggestions URL"


admin.site.register(Product)
admin.site.register(PaymentMethod)
admin.site.register(Category)
admin.site.register(DailySpecial)
admin.site.register(Promotion)
admin.site.register(Client, ClientAdmin)
