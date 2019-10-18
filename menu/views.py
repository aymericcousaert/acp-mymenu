from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic, View

from menu.models import Product


class Index(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('My menu!')


class ProductListView(generic.ListView):
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()
