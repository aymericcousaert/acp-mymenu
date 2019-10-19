from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic, View
from .forms import ProductForm
from .models import Product


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
