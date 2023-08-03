from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='아이디')
    username_check = forms.BooleanField(required=True, initial=False, widget=forms.HiddenInput, label='아이디 중복확인')
    password1 = forms.CharField(widget=forms.PasswordInput, label='비밀번호')
    password2 = forms.CharField(widget=forms.PasswordInput, label='비밀번호 확인')
    fullname = forms.CharField(max_length=30, label='이름')
    year = forms.CharField(max_length=4, label='년도')
    month = forms.CharField(max_length=2, label='월')
    day = forms.CharField(max_length=2, label='일')
    address = forms.CharField(max_length=100, label='주소')
    detailed_address = forms.CharField(max_length=100, label='상세주소')
    phone_number = forms.CharField(max_length=13, label='전화번호')
    email = forms.EmailField(label='이메일')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'username_check', 'password1', 'password2', 'fullname',
                    'address', 'detailed_address', 'phone_number', 'email')