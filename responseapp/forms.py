
from django import forms


class MyForm(forms.Form):
 name = forms.CharField(label='Enter your name', max_length=100)
 email = forms.EmailField(label='Enter your email', max_length=100)
 password = forms.CharField(label='Enter your password', widget=forms.PasswordInput())
 mobilenumber = forms.CharField(label='Enter your mobile number', max_length=10)
