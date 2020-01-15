from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView


from create_wed.forms import SignUpForm, LoginForm, CreateWeddingForm, ContactUsForm

# Create your views here.
from create_wed.models import Wedding


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.warning(request, f"{form.cleaned_data['username']} is already in use")
                return redirect(reverse('signup'))
            user = User.objects.create_user(**form.cleaned_data)
            messages.info(request, f'{user.username} successfully created!')
            return redirect(reverse('create_wed/login'))
    else:
        form = SignUpForm()

    return render(request, 'create_wed/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                messages.info(request, 'Successfully logged in!')
                return redirect(reverse('create_wed:home'))
            else:
                messages.error(request, 'Bad authentication...')
                return redirect(reverse('create_wed:login'))
    else:
        form = LoginForm()

    return render(request, 'create_wed/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect(reverse('create_wed:home'))

# @login_required
def home(request):
    return render(request, 'create_wed/index.html')


@login_required
def create_weeding_view(request):
    if request.method == 'POST':
        form = CreateWeddingForm(request.POST)
        print(form.errors)
        if form.is_valid():
            wedding = Wedding(user=request.user,**form.cleaned_data)
            wedding.save()
            messages.info(request, 'Wedding successfully created!')
            return redirect(reverse('create_wed:services'))
    else:
        form = CreateWeddingForm()

    return render(request, 'create_wed/create_wedding.html', {'form': form})


def services(request):
    return render(request, 'create_wed/services.html')


class ContactUs(CreateView):
    form_class = ContactUsForm
    template_name = 'create_wed/contact.html'
    success_url = '/create_wed/home'
