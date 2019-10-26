from django import forms

from menu.models import PaymentMethod, Category, Product


class ProductForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"] = forms.ChoiceField(label='Category', required=False, choices=
    [("-", "-")] + [(category.name, category.name) for category in Category.objects.all()])

    name = forms.CharField(label='Nombre', required=True, max_length=30,
                           error_messages={'required': 'Este campo es requerido',
                                           'invalid': 'Debe tener como maximo 30 caracteres'})
    description = forms.CharField(label='Descripción', required=True, max_length=500,
                                  error_messages={'required': 'Este campo es requerido',
                                                  'invalid': 'Debe tener como maximo 500 caracteres'})
    price = forms.DecimalField(label='Precio', required=True, decimal_places=2, max_digits=6,
                               error_messages={'required': 'Este campo es requerido',
                                               'invalid': 'Debe tener como maximo 6 digitos'})
    suitForVegetarian = forms.ChoiceField(label='Apto para vegetarianos', required=True, choices=[("Si", "Si"),
                                                                                                  ("No", "No")])
    suitForGlutenIntolerant = forms.ChoiceField(label='Apto para celíacos', required=True, choices=[("Si", "Si"),
                                                                                                    ("No", "No")])



class PaymentMethodForm(forms.Form):
    description = forms.CharField(label='Descripción', required=True, max_length=200,
                                  error_messages={'required': 'Este campo es requerido',
                                                  'invalid': 'Debe tener como maximo 200 caracteres'})
    payment_type = forms.ChoiceField(label='Tipo de pago', required=True, choices=PaymentMethod.TYPES,
                                     error_messages={'required': 'Este campo es requerido'})


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(forms.ModelForm, self).clean()

        # extract the username and text field from the data
        name = self.data.get('name')

        # conditions to be met for the username length
        if len(name) < 1:
            self._errors['name'] = self.error_class([
                'El nombre es requerido y debe ser como maximo de longitud 30'])

        # return any errors if found
        return self.cleaned_data


class SelectProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"] = forms.ChoiceField(choices=[(product.name, product.name) for product in Product.objects.filter(category__name__isnull=True)])

    def clean(self):
        return self.cleaned_data
