from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):

    if request.method == 'POST':
        # extracts the user form's input
        username = request.POST['username']
        password = request.POST['password']

        # checks the user credentials with our db record
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # for testing
        # print('this is the post method')

        # extracts the user form's inputs
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists.')
                    return redirect('register')
                else:
                    # if all conditionss are satisfied, we save the new user
                    user = User.objects.create_user(
                        first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user)
                    # if you want the user to be logged in automatically
                    # messages.success(request, 'You are now logged in.')
                    # return redirect('dashboard')
                    user.save()
                    messages.success(
                        request, 'You are successfully registered.')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords dont match.')
            return redirect('register')

        # # this calls the error message functionality with INCLUDES\MESSAGES.HTML
        # messages.error(request, 'This is error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

# requires a login before we can use the dashboard


@login_required(login_url='login')
def dashboard(request):
    # extracts all the car inquiries of a logged in user.
    user_inquiry = Contact.objects.order_by(
        '-create_date').filter(user_id=request.user.id)
    data = {
        'inquiries': user_inquiry,
    }

    return render(request, 'accounts/dashboard.html', data)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # add this only if you want this message to show on the home page
        # messages.success(request, 'You are successfully logged out.')
        return redirect('home')
    return redirect('home')
