from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm()
        if form.is_valid():
            cd = form.cleaned_data
            # Check if User is active in database, return User object
            user = authenticate(username=cd['username'], password=cd['password'])

        if user is not None:
            if user.is_active:
                login(request, user)        # Add User to current session
                return HttpResponse('Authentication successfully')
            else:
                return HttpResponse('Account is blocked')
        else:
            return HttpResponse('Wrong authentication data')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {
                  'form' : form
    })