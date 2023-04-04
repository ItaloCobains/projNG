from django import forms

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu usuário')
        add_placeholder(self.fields['password'], 'Senha')

    
    
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    username = forms.CharField(
        label='Usuário',
        error_messages={
            'required': 'Usuário não deve estar vazio.',
            'min_length': 'O nome de usuário deve ter pelo menos 4 caracteres.',
        },
        min_length=4, max_length=150,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Senha',
        error_messages={
        'required': 'A senha não deve estar vazia.',
        },
    )
