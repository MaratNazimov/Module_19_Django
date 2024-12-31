from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин")
    password = forms.CharField(max_length=8, label="Введите пароль")
    repeat_password = forms.CharField(max_length=8, label="Повторите пароль")
    age = forms.IntegerField(label="Введите свой возраст")
    subscribe = forms.BooleanField(required=False, label="Согласие на обработку персональных данных")

