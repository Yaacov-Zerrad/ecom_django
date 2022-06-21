from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .form import UserForm

def login_user(request):
    error = ''
    title = 'Login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_doctor:
                return redirect('doctor')
            elif user.is_infirmiere:
                return redirect('infirmiere')
            elif user.is_patient:
                return redirect('patient')
        else: 
            error = 'password or username not correct'
    return render(request, "users/login.html", {'error': error, 'title':title})

def doctor(request):
    return render (request, 'users/doctor.html')

def infirmiere(request):
    return render (request, 'users/infirmiere.html')

def patient(request):
    return render (request, 'users/patient.html')

def register(request):
    title = 'Register'
    form = UserForm()
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'users/register.html', {'form':form, 'title':title})
        

    
