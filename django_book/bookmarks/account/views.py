from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
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
                  'form': form
    })


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {
        'section': dashboard
    })


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # We create new object, without saving
            new_user = user_form.save(commit=False)         # save method used on form
            # Set a password from form
            new_user.set_password(user_form.cleaned_data['password'])
            # saving object to database
            new_user.save()
            return render(request, 'account/registration_done.html', {
                'new_user': new_user
            })
    else:
        user_form = UserRegistrationForm()

    return render(request, 'account/registration.html', {
        'user_form': user_form
    })