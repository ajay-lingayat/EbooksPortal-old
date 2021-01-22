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
    first_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Firstname',}))
    last_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Lastname',}))
    captcha = ReCaptchaField()

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class ProfileForm(forms.Form):
    firstname = forms.CharField(max_length=15, widget=TextInput())
    lastname = forms.CharField(max_length=15, widget=TextInput())
    email = forms.EmailField(widget=TextInput())
    username = forms.CharField(max_length=15, widget=TextInput())