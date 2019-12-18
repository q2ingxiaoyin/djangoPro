from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length = 32)
    email = forms.EmailField()
    password = forms.CharField(max_length = 32)
    picture = forms.ImageField()