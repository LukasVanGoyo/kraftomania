from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib import messages
from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import  urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from . tokens import account_activation_token

def home(request):

   
    return render(request, 'base.html')


def activate(request, uid64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Twoje konto zostało aktywowane. Możesz się teraz zalogować')
        return redirect('/login')
    else:
        messages.error(request, 'Link aktywacyjny jest nieprawidłowy')

    return redirect('/')








def activateEmail(request, user, to_email):
    mail_subject = "Aktywuj swoje konto"
    message = render_to_string("activation_email.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'

    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'{user.username} wejdź na swojego maila {to_email} i aktywuj konto.' )
    else:
        messages.error(request, 'Problem z wysłaniem maila z linkiem aktywacyjnym. Sprawdź czy podałeś prawidłowy adres email.')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Zostałeś pomyślnie zarejestrowany')
            return redirect('/')
        
        else:
            messages.error(request, "Wpisane hasło lub email są nieprawidłowe")
        
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            activateEmail(request, user, form.cleaned_data.get('email'))
            messages.success(request, 'Zostałeś zarejestrowany jako  ' + user.username )
                
    else: 
        form = RegisterUserForm()      
    
    return render(request, 'register.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "Zostałeś wylogowany")
    return redirect('/')


def user_profile(request):
    return render(request, 'user_profile.html')