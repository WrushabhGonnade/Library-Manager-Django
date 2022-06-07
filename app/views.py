from django.shortcuts import render, redirect
from django.views import View

from app.forms import Book_Form, Register_Form
from app.models import book, LoginInfo_Table
from django.contrib import messages


def newbook(request):
    if request.method == 'POST':
        form = Book_Form(request.POST)
        if form.is_valid:
            try:
                form.save()
                messages.success(request, 'Book added to database')

            except:
                pass
    form = Book_Form()
    return render(request, 'newbook.html', {'form': form})


def display(request):
    data = book.objects.all()
    print(data)
    return render(request, 'show.html', {'data': data})


def emp_login(request):
    return render(request, 'login.html')


def check(request):
    name = request.POST['u']
    passwd = request.POST['up']

    print(name)
    print(passwd)
    dat = LoginInfo_Table.objects.all()
    for e in dat.iterator():

        if e.email == name and e.passwd == passwd:
            print('Logged In')
            return redirect('/welcomeadmin')

    print('Nooo')
    messages.info(request, 'Wrong Credentials, Please check and try again')

    return redirect('/emp_login')


def signup(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        passwd = request.POST.get('passwd')
        fname = request.POST.get('fname')
        if email=='' or passwd=='' or fname=='':
            print('No Data')
            messages.warning(request, 'One or more fields are empty, please enter correct data')
            return redirect('/c')

        form = LoginInfo_Table(email=email, passwd=passwd,name=fname)
        dat = LoginInfo_Table.objects.all()
        for i in dat.iterator():
            if email == i.email:
                print('No')
                messages.warning(request, 'User with same Email already exist, please login')
                return redirect('/c')
        messages.success(request, 'Congratulations..Registered Successfully')
        form.save()
    return render(request, 'register.html')


def home1(request):
    return render(request, 'home1.html')


def adminlogin(request):
    data = book.objects.all()
    print(data)
    return render(request, 'adminlogin.html', {'data': data})


def delete(request, id):
    data = book.objects.get(id=id)
    print(data)
    data.delete()
    return redirect('/adminlogin')


def edit(request, id):
    data = book.objects.get(id=id)
    return render(request, 'edit.html', {'book': data})


def update(request, id):
    data = book.objects.get(id=id)
    form = Book_Form(request.POST, instance=data)
    form.save()
    return redirect('/adminlogin')


def welcomeadmin(request):
    return render(request, 'welcomeadmin.html')



