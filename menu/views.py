from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib import messages

from .models import Product, Category, PaymentMethod, Promotion, Client, Suggestion
from .forms import SuggestionForm

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


class FormSuggestionsView(View):
    template_name = 'form_suggestions.html'

    def get(self, request, token_url):
        form = SuggestionForm()
        client = Client.objects.filter(token=token_url)

        if client:
            return render(request, self.template_name, {'form': form})
        else:
            # TODO: este mensaje me lo muestra tmb luego de enviar los comentarios
            # messages.warning(request, 'Este link es inválido o ya fue utilizado')
            return render(request, 'index.html')

    def post(self, request, token_url):

        form = SuggestionForm(request.POST)

        if form.is_valid():
            # Almaceno la sugerencia en la base de datos
            client = Client.objects.filter(token=token_url)[0]
            form.cleaned_data['client'] = client
            Suggestion.objects.create(**form.cleaned_data)
            messages.success(request, '¡Comentario enviado exitosamente!')

            # Limpio el token del cliente asi no lo puede volver a utilizar
            client.token = ''
            client.save()

            return redirect('index.html')

        return render(request, self.template_name, {'form': form})
