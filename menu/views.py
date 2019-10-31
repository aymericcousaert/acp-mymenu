from django.shortcuts import render
from django.views import generic, View

from .models import Product, Category, PaymentMethod, Promotion

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ProductListView(generic.ListView):
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


class ProductDescription(View):
    model = Product
    template_name = 'product/description.html'

    def get(self, request, pk):
        product = Product.objects.filter(pk=pk)
        return render(request, self.template_name, {'product': product[0]})


class PaymentMethodListView(generic.ListView):
    template_name = 'payments.html'
    context_object_name = 'payments'

    def get_queryset(self):
        return PaymentMethod.objects.all()


class CategoryListView(generic.ListView):
    template_name = 'categories.html'
    context_object_name = 'elements'

    def get_queryset(self):
        return {'categories': Category.objects.all(), 'products': Product.objects.all()}


class PromotionListView(generic.ListView):
    template_name = 'promotions.html'
    context_object_name = 'promotions'

    def get_queryset(self):
        return Promotion.objects.all()




