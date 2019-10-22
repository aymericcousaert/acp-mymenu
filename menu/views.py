from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic, View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import ProductForm, PaymentMethodForm
from .models import Product, PaymentMethod


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
            Product.objects.create(**form.cleaned_data)
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





