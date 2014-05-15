from django import forms
from django.forms import ModelForm
from models import Client,Factory,Car
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2","first_name","last_name")
        

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password","first_name","last_name")


class FactoryForm(ModelForm):
    class Meta:
        model = Factory

class ClientForm(ModelForm):
    class Meta:
        model = Client

class CarForm(ModelForm):
    class Meta:
        model = Car





