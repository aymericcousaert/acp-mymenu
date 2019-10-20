from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic, View

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


class PaymentMethodView(View):

    def get(self, request):
        form = PaymentMethodForm()
        return render(request, 'paymentMethod.html', {'form': form})

    def post(self, request):
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            PaymentMethod.objects.create(**form.cleaned_data)
            messages.success(request, 'Metodo de pago creado exitosamente')
            return render(request, 'paymentMethod.html', {'form': PaymentMethodForm()})
        return render(request, 'paymentMethod.html', {'form': form})


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
