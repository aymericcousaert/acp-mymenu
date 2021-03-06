from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib import messages

from .models import Product, Category, PaymentMethod, Promotion, Client, Suggestion, DailySpecial
from .forms import SuggestionForm

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Index(View):
    def get(self, request, *args, **kwargs):
        return redirect('products')


class ProductListView(View):
    template_name = 'products.html'

    def get(self, request, pk=None):
        active_pk = pk
        categories = Category.objects.all()

        if categories:
            active_pk = pk or categories[0].pk

        products = Product.objects.filter(category_id=active_pk)
        context = {'products': products, 'categories': categories,
                   'active_pk': active_pk, 'specials': DailySpecial.objects.all()}

        return render(request, self.template_name, context)


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
            messages.warning(request, 'Este link es inválido o ya fue utilizado')
            return redirect('index')

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

            return redirect('index')

        return render(request, self.template_name, {'form': form})
