from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from cars.models import Car


def register_view(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password_1']
        confirm = request.POST['password_2']

        try:
            if password == confirm:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists.')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'Email already exists.')
                    else:
                        user = User.objects.create_user(
                            first_name=firstname,
                            last_name=lastname,
                            username=username,
                            email=email,
                            password=password
                        )

                        user.save()
                        messages.success(request, 'You are now registered.')
                        auth.login(request, user)
                        messages.success(request, 'You are now logged in.')
            else:
                messages.error(request, 'Passwords do not match.')
        except ValueError:
            messages.error(request, 'Fields must not be empty.')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        
    return redirect('login')

@login_required
def dashboard_view(request):
    user = request.user
    cars = Car.objects.all()
    return render(request, 'accounts/dashboard.html', {'user': user, 'cars': cars})
