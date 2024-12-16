from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from auth_system.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("phone_number", "first_name", "last_name")

class CustomUserAuthenticationForm(AuthenticationForm):
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'phone_number')
