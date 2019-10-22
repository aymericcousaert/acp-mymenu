from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic, View

from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import ProductForm, PaymentMethodForm
from .models import Product, PaymentMethod

from .forms import ProductForm, CategoryForm, SelectProductForm
from .models import Product, Category

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


class PaymentMethodListView(generic.ListView):
    template_name = 'payment_method_list.html'
    context_object_name = 'payments'

    def get_queryset(self):
        return PaymentMethod.objects.all()


class PaymentMethodView(View):

    def get(self, request):
        form = PaymentMethodForm()
        return render(request, 'payment_method.html', {'form': form})

    def post(self, request):
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            PaymentMethod.objects.create(**form.cleaned_data)
            messages.success(request, 'Metodo de pago creado exitosamente')
            return redirect('payment_list')
        return render(request, 'payment_method.html', {'form': form})


class CreateProductView(View):

    def get(self, request):
        form = ProductForm()
        return render(request, 'product/create.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['category']
            categoryFound = False
            for val in Category.objects.all():
                if val.name == name:
                    category = val
                    categoryFound = True
            if categoryFound:
                Product.objects.create(name=form.cleaned_data['name'], description=form.cleaned_data['description'],
                                   price=form.cleaned_data['price'], category=category)
            else:
                Product.objects.create(name=form.cleaned_data['name'], description=form.cleaned_data['description'],
                                   price=form.cleaned_data['price'])
            messages.success(request, 'Producto creado exitosamente')
            return render(request, 'product/create.html', {'form': ProductForm()})
        return render(request, "product/create.html", {'form': form})


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('products')


class CreateUserView(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'user/create.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request, 'Usuario creado exitosamente')
            return render(request, 'user/create.html', {'form': UserCreationForm()})
        return render(request, "user/create.html", {'form': form})


class CategoryListView(generic.ListView):
    template_name = 'categories.html'
    context_object_name = 'elements'

    def get_queryset(self):
        return {'categories': Category.objects.all(), 'products': Product.objects.all()}



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
