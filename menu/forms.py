from django import forms
from menu.models import PaymentMethod


class ProductForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, max_length=30,
                           error_messages={'required': 'Este campo es requerido',
                                           'invalid': 'Debe tener como maximo 30 caracteres'})
    description = forms.CharField(label='Descripción', required=True, max_length=500,
                                  error_messages={'required': 'Este campo es requerido',
                                                  'invalid': 'Debe tener como maximo 500 caracteres'})
    price = forms.DecimalField(label='Precio', required=True, decimal_places=2, max_digits=6,
                               error_messages={'required': 'Este campo es requerido',
                                               'invalid': 'Debe tener como maximo 6 digitos'})


class PaymentMethodForm(forms.Form):

    description = forms.CharField(label='Descripción', required=True, max_length=200,
                                  error_messages={'required': 'Este campo es requerido',
                                                  'invalid': 'Debe tener como maximo 200 caracteres'})
    payment_type = forms.ChoiceField(label='Tipo de pago', required=True, choices=PaymentMethod.TYPES,
                                     error_messages={'required': 'Este campo es requerido'})
