from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(
            widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'enter your full name'
                }
            )
        )
    email    = forms.EmailField(
            widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'enter your email'
                }
            )
        )
    content  = forms.CharField(
            widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'placeholder': 'enter your message'
                }
            )
        )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
