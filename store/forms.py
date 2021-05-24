from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from store.models import NewsLetterRecipientEmail
# from captcha.fields import CaptchaField, CaptchaTextInput


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': "contact_input"}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': "contact_input"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "contact_input"}))
    password2 = forms.CharField(label='Подтверждения пароля',
                                widget=forms.PasswordInput(attrs={'class': "contact_input"}))
    # captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'contact_input'}),
            'email': forms.EmailInput(attrs={'class': 'contact_input'}),
            'password1': forms.PasswordInput(attrs={'class': 'contact_input'}),
            'password2': forms.PasswordInput(attrs={'class': 'contact_input'}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': "contact_input"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "contact_input"}))
    # captcha = CaptchaField()


class ContactForm(forms.Form):
    first_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': "contact_input"}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': "contact_input"}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class': "contact_input"}))
    message = forms.CharField(label='Message', widget=forms.TextInput(attrs={'class': "contact_input contact_textarea"}))
    # captcha = CaptchaField()


''' Email рассылка'''
''' Решить вопрос сохранения уникальных email-ов в БД '''
class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterRecipientEmail
        fields = ("email", )
        widgets = {
            "email": forms.EmailInput(attrs={"class": "newsletter_input", "placeholder": "Your Email"})
        }
        labels = {
            "email": ''
        }