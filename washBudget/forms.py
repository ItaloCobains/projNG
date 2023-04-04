from django import forms
from django.forms import RadioSelect


class SofaForm(forms.Form):
    num_pessoas = forms.ChoiceField(choices=[(i, i) for i in range(2, 13)], widget=forms.RadioSelect(attrs={'class': 'hidden'}))
    modelo = forms.ChoiceField(choices=[
        ('retratil', 'Sofá Retrátil'),
        ('comum', 'Sofá Comum'),
        ('canto', 'Sofá de Canto'),
        ('chaise', 'Sofá com Chaise'),
        ('cama', 'Sofá-Cama'),
        ('cantoalemao', 'Canto Alemão'),
        ('namoradeira', 'Namoradeira'),
        ('diva', 'Divã')
    ], widget=forms.RadioSelect())
    material = forms.ChoiceField(choices=[('tecido', 'Tecido')], widget=forms.RadioSelect())
    servicos = forms.MultipleChoiceField(choices=[
        ('limpeza', 'Limpeza'),
    ], widget=forms.CheckboxSelectMultiple())

