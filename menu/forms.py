from django import forms
from .models import Suggestion


class SuggestionForm(forms.Form):
    description = forms.CharField(label='Comentario y/o sugerencia', required=True, max_length=500,
                                  error_messages={'required': 'Por favor, ingrese algún comentario y/o sugerencia',
                                                  'invalid': 'Por favor, no supere los 500 caracteres'})
