from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateForm, RegistForm
from app1.models import Register, create_an_account
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        account = create_an_account.objects.filter(email=request.POST.get('email')).exists()
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_user = Register.objects.filter(email=email, password=password)

        for data in check_user:
            print("Filter data ", check_user)
            if data.email == email:
                if data.password == password:
                    return render(request, 'create.html')
                else:
                    return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')


def bankindex(request):
    return render(request, 'bankindex.html')


def banklogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_user = create_an_account.objects.filter(email=email)
        for data in check_user:
            print("Filter data ", check_user)
            if data.email == email:
                if data.password == password:
                    return render(request, 'bankindex.html')
                else:
                    return HttpResponse('Please enter valid Username or Password.')
    return render(request, 'banklogin.html')


def bankcreate(request):
    return render(request, 'create.html')


def logout(request):
    return render(request, 'index.html')


def register(request):
    form = RegistForm(request.POST)
    if request.method == "POST":

        password1 = request.POST['password']
        password2 = request.POST['confirm_password']

        if password1 != password2:
            return HttpResponse(request, "Password does not match")
        else:
            if form.is_valid():
                form.save()
                return render(request, "login.html")
    return render(request, "register.html", context={"form": form})

def CreateAccount(request):
    form = CreateForm(request.POST)
    if request.method == "POST":

        password1 = request.POST['password']
        password2 = request.POST['confirm_password']

        if password1 != password2:
            return HttpResponse(request, "Password does not match")

        if create_an_account.objects.filter(email=request.user.email).exists():
            return HttpResponse(request,"User Already exists")
        else:
            if form.is_valid():
                print(request.user)
                print("Test")
                reg_user = Register.objects.get(id=request.user.id)
                new_id = form.save()
                new_key = create_an_account.objects.get(id=new_id.pk)
                new_key.Register=reg_user
                new_key.save()
                return render(request, "banklogin.html")
    return render(request, "create_an_account.html", context={"form": form})


def TransferMoney(request):
    return render(request, 'TransferMoney.html')


def Deposite(request):
    return render(request, 'Deposite.html')


def Withdrawl(request):
    return render(request, 'Withdrawl.html')


def TransectionDetails(request):
    return render(request, 'TransectionDetails.html')


def BalanceEnquiry(request):
    return render(request, 'BalanceEnquiry .html')


def ViewProfile(request):
    return render(request, ' ViewProfile.html')
