from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False

    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        super(forms.ModelForm, self).clean()

        # extract the username and text field from the data
        name = self.data.get('name')
        description = self.data.get('description')
        price = self.data.get('price')

        # conditions to be met for the username length
        if len(name) < 1:
            self._errors['name'] = self.error_class([
                'El nombre es requerido y debe ser como maximo de longitud 30'])
        if len(description) < 1:
            self._errors['description'] = self.error_class([
                'La descripcion es requerido y debe ser como maximo de longitud 500'])
        if len(price) < 1:
            self._errors['price'] = self.error_class([
                'El precio es requerido'])

        # return any errors if found
        return self.cleaned_data


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
    #name = forms.ChoiceField(choices=[(product.pk, product.name) for product in Product.objects.all()])
    name = forms.CharField()

    def clean(self):
        # extract the username and text field from the data
        name = self.data.get('name')

        found = False

        for product in Product.objects.all():
            if product.name == name:
                found = True

        if not found:
            self._errors['name'] = self.error_class([
                'El product no existe'])

        # return any errors if found
        return self.cleaned_data




