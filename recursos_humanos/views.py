from django.shortcuts import render,redirect
from .models import Employee
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('http://127.0.0.1:8000')  # Redirigir a la página de inicio después del inicio de sesión
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')

    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'registro.html', {'form': form})


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']
            return render(request, 'exito.html')
    else:
        form = ContactForm()

    return render(request, 'contacto.html', {'form': form})

@login_required(login_url='/registro/')
def lista_empleados(request):
    employees = Employee.objects.all()
    businessentityid = request.GET.get('businessentityid')
    jobtitle = request.GET.get('jobtitle')
    gender = request.GET.get('gender')
    if businessentityid:
        employees = employees.filter(businessentityid__businessentityid=businessentityid)
    if jobtitle:
        employees = employees.filter(jobtitle__icontains=jobtitle)
    if gender:
        employees = employees.filter(gender=gender)
    context = {'employees': employees}
    return render(request, 'empleados.html', context)


def index(request):
    return render(request,'index.html')

def nosotros(request):
    return render(request,'nosotros.html')

def user_logout(request):
    logout(request)
    return redirect('index')
