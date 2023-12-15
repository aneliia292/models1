from django import forms



class UserLoginForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': "email"}))

    password = forms.CharField(widget=forms.TextInput(attrs={'class': "password"}))