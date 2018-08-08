from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm

def home_page(request):
    context = {'title': 'The Title'}
    return render(request, 'home_page.html', context)

def about_page(request):
    return render(request, 'about_page.html', {})

def contact_page(request):
    contact_form = ContactForm()
    context = {
        'title': 'Contact page',
        'form': contact_form
    }
    return render(request, 'contact/view.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            form = LoginForm()
            return redirect('/login')
        else:
            print('Error')

    return render(request, 'auth/login.html', {'form': form})

def register(request):
    return render(request, 'auth/register', {})
