
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ValidationError
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginForm(AuthenticationForm):
    
    username = forms.EmailField(max_length=20, label='Email Address', required=True)


    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(email=email)
            result = authenticate(username= user.username, password= password)
            print(result)
            if result:
                login(self.request, result)
                return result
            else:
                raise ValidationError('email or password invalid1')
        except:
            raise ValidationError('email or password invalid2')




  