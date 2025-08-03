from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

class SignUpform(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password"]



