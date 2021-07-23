from courses import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']


    def clean_email(self):
        print('cleaning')
        email = self.cleaned_data['email']
        print(email)
        user = None
        try:
            user = User.objects.get(email = email)
            print(user)
        except:
            print('fail')
            return email

        if user is not None:
            raise ValidationError('email exists')