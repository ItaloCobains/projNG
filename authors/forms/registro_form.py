from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)

class RegisterForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("As senhas não coincidem."),
        'username_taken': _("Este nome de usuário já está em uso."),
        'email_taken': _("Este e-mail já está em uso."),
        'invalid_email': _("Por favor, insira um endereço de e-mail válido."),
        'password_too_short': _("A senha deve ter no mínimo 8 caracteres."),
        'password_common': _("Por favor, escolha uma senha mais forte."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu usuário')
        add_placeholder(self.fields['email'], 'Seu e-mail')
        add_placeholder(self.fields['first_name'], 'Seu nome')
        add_placeholder(self.fields['last_name'], 'Seu sobrenome')
        add_placeholder(self.fields['password'], 'Senha')
        add_placeholder(self.fields['password2'], 'Confirmar senha')

    first_name = forms.CharField(
        error_messages={'required': 'Digite seu nome.'},
        label='Nome',
    )

    last_name = forms.CharField(
        error_messages={'required': 'Digite seu sobrenome.'},
        label='Sobrenome',
    )

    username = forms.CharField(
        label='Usuário',
        error_messages={
            'required': 'Usuário não deve estar vazio.',
            'duplicate_username': 'Este nome de usuário já está em uso.',
            'min_length': 'O nome de usuário deve ter pelo menos 4 caracteres.',
        },
        min_length=4, max_length=150,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Senha',
        error_messages={'required': 'A senha não deve estar vazia.'},
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirmar senha',
        error_messages={'required': 'Por favor, repita sua senha.'},

    )

    email = forms.EmailField(
        error_messages={
            'required': 'O E-mail não deve estar vazio.',
            'invalid': 'Por favor, insira um endereço de e-mail válido.'
        },
        label=_('E-mail')
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Usuário',
            'email': 'E-mail',
            'password': 'Senha',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            password_confirmation_error = ValidationError(
                'As senhas devem ser iguais.',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
        elif len(password) < 4:
            
            raise ValidationError({
                    'password': 'A senha deve conter pelo menos 4 caracteres.',
                    'password2': 'A senha deve conter pelo menos 4 caracteres.',

                })
    
    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'O e-mail já está em uso.', code='invalid',
            )

        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        exists = User.objects.filter(username=username).exists()

        if exists:
            raise ValidationError(
                'Este nome de usuário já está em uso.', code='duplicate_username',
            )

        return username
    

    