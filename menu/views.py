from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic, View
from django.views.generic import TemplateView

from .forms import ProductForm, CategoryForm, SelectProductForm
from .models import Product, Category

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Index(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('My menu!')


class ProductListView(generic.ListView):
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


# New product view
def newproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            # Redirect back to the same page if the data
            # was invalid
            return render(request, "product.html", {'form': form})
    form = ProductForm()
    return render(request, 'product.html', {'form': form})


class CategoryListView(generic.ListView):
    template_name = 'categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


# New category view
def newCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            # Redirect back to the same page if the data
            # was invalid
            return render(request, "category.html", {'form': form})
    form = CategoryForm()
    return render(request, 'category.html', {'form': form})


class SelectProduct(TemplateView):
    template_name = 'productChoice.html'

    def get(self, request, category):
        form = SelectProductForm()
        return render(request, self.template_name, {'form': form, 'div': False})

    def post(self, request, category):
        form = SelectProductForm(request.POST)
        div = False
        if request.method == "POST":
            if form.is_valid():
                name = form.cleaned_data['name']
                for val in Product.objects.all():
                    if val.name == name:
                        product = val
                categoryToAssign = Category.objects.filter(name__exact=category)[0]
                product.category = categoryToAssign
                product.save()
            div = True
        return render(request, self.template_name, {'form': form, 'div': div})
