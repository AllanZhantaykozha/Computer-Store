from django import forms
from .models import News, PC, Accessory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your title here'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your text here', 'rows': '3'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'id': 'formFile'}),
        }


class PCForm(forms.ModelForm):
    class Meta:
        model = PC
        fields = ['title', 'content', 'cpu', 'gpu', 'ram', 'memory', 'price', 'photo', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your title here'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your text here', 'rows': '3'}),
            'cpu': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your cpu here'}),
            'gpu': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your gpu here'}),
            'ram': forms.NumberInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your ram here'}),
            'memory': forms.NumberInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your memeory here'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your price here'}),          
            'photo': forms.FileInput(attrs={'class': 'form-control', 'id': 'formFile'}),
        }


class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['title', 'content', 'types', 'price', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your title here'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your text here', 'rows': '3'}),
            'types': forms.Select(attrs={'class': 'form-select', 'aria-label': 'Select type'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'Write your price here'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'id': 'formFile'}),
        }


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))    
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


