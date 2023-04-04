from django import forms
from .models import Sofa

class SofaForm(forms.ModelForm):
    class Meta:
        model = Sofa
        fields = ['num_pessoas', 'modelo', 'material', 'servicos']


