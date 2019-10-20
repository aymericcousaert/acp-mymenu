from django import forms
from .models import Product, PaymentMethod


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        super(forms.ModelForm, self).clean()

        # extract the username and text field from the data
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')

        # conditions to be met for the username length
        if not name or len(name) < 1:
            self._errors['name'] = self.error_class([
                'El nombre es requerido y debe ser como maximo de longitud 30'])
        if not description or len(description) < 1:
            self._errors['description'] = self.error_class([
                'La descripcion es requerido y debe ser como maximo de longitud 500'])
        if not price or price == 0:
            self._errors['price'] = self.error_class([
                'El precio es requerido'])

        # return any errors if found
        return self.cleaned_data


class PaymentMethodForm(forms.Form):

    CASH = 'CA'
    CREDIT = 'CC'
    DEBIT = 'DB'

    TYPES = [
        (CASH, 'Efectivo'),
        (CREDIT, 'Credito'),
        (DEBIT, 'Debito'),
    ]

    description = forms.CharField(label='Descripción', required=True, max_length=200,
                                  error_messages={'required': 'Este campo es requerido',
                                                  'invalid': 'Debe tener como maximo 200 caracteres'})
    payment_type = forms.ChoiceField(label='Tipo de pago', choices=TYPES, required=True,
                                     error_messages={'required':'Este campo es requerido'})
