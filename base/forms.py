from django import forms
from django.forms import TextInput, Textarea

from allauth.account.forms import SignupForm

from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=15, widget=TextInput())
    lastname = forms.CharField(max_length=15, widget=TextInput())
    email = forms.EmailField(widget=TextInput())
    subject = forms.CharField(max_length=50, widget=TextInput())
    message = forms.CharField(max_length=500, widget=Textarea())


class CustomSignUpForm(SignupForm):
    first_name = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Firstname',
            }
        )
    )
    last_name = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Lastname',
            }
        )
    )
    captcha = ReCaptchaField()

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user



class ProfileForm(forms.Form):
    firstname = forms.CharField(
        max_length=15,
        widget=TextInput(
            attrs={
                'placeholder': 'Firstname',
                'autocomplete': 'off',
                'required': '',
                'class': 'form-control',
            }
        )
    )
    lastname = forms.CharField(
        max_length=15,
        widget=TextInput(
            attrs={
                'placeholder': 'Lastname',
                'autocomplete': 'off',
                'required': '',
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        widget=TextInput(
            attrs={
                'placeholder': 'Email',
                'autocomplete': 'off',
                'required': '',
                'class': 'form-control',
            }
        )
    )
    username = forms.CharField(
        max_length=15,
        widget=TextInput(
            attrs={
                'placeholder': 'Username',
                'autocomplete': 'off',
                'required': '',
                'class': 'form-control',
            }
        )
    )