from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio']
        widgets = {'bio': forms.Textarea()}

    # Any validation here is only client-side so that the user knows. It does not validate server side
    password = forms.CharField(label='Password',widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput())
