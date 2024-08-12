from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request=request, template_name='accounts/login.html')


def logout(request):
    auth.logout(request)
    # messages.success(request, 'You are now logged out')
    return redirect('home')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,
                                                    last_name=lastname,
                                                    username=username,
                                                    email=email,
                                                    password=password)
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('dashboard')
                    user.save()
                    messages.success(request, 'Account created')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request=request, template_name='accounts/register.html')


# Only for authenticated user
@login_required(login_url='login')
def dashboard(request):
    user_inquiry = Contact.objects.all().order_by('-create_date').filter(user_id=request.user.id)
    context = {
        'user_inquiry': user_inquiry,
    }
    return render(request=request, template_name='accounts/dashboard.html', context=context)