from django.shortcuts import render, redirect
from operation.models import Employees

def index(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'index.html', context)

def Add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees.objects.create(
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()

    return redirect('index')

def Edit(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'edit.html', context)

def Update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
        id=id,
        name = name,
        email = email,
        address = address,
        phone = phone,
        )
        emp.save()

    return redirect('index')


def Delete(request, id):
    emp = Employees.objects.filter(id=id)
    emp.delete()
    return redirect('index')