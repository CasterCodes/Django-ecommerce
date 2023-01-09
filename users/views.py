from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

def signup(request):
    return render(request=request, template_name='signup.html')

def signin(request):
    if request.method == 'POST':
        username_email = request.POST.get('username_email')
        password = request.POST.get('password')

        if username_email == '' or password == '':
            messages.info(request=request, extra_tags=messages.ERROR, message='All the fields must be filled')
            return redirect('/users/signin')

        user = authenticate(username_email=username_email, password=password)

        if user is None:
            messages.info(request=request, extra_tags=messages.ERROR, message='Provided wrong credentials')
            return redirect('/users/signin')

        login(request=request, user=user)

        return redirect('/')

    else:
        return render(request=request, template_name='signin.html')
