from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from django.contrib.auth import get_user_model

User = get_user_model()

INPUT_CLASS = "w-full border border-slate-300 rounded px-3 py-2 text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-amber-400 focus:border-amber-400 transition-colors"


def style_fields(form_instance):
    """Add theme classes + a safe placeholder (never 'None') to every field."""
    for field_name, field in form_instance.fields.items():
        placeholder = field.label or field_name.replace('_', ' ').title()
        field.widget.attrs.update({
            'class': INPUT_CLASS,
            'placeholder': placeholder,
        })


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False, label='Phone')
    profile_picture = forms.ImageField(required=False, label='Profile picture')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'profile_picture', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)


class CustomUserChangeForm(UserChangeForm):
    password = None  # edit form-e password field dekhate chai na
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False, label='Phone')
    profile_picture = forms.ImageField(required=False, label='Profile picture')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)