from django.shortcuts import render
from webapp.models import salaries,dept_emp,departments,Employees,titles
from . import forms


# Create your views here.
def base_view(request):
    return render(request,'base.html')
def Employees_view(request):
    form = forms.EmployeesForm()
    if request.method=='post':
        form = forms.EmployeesForm(request.POST)
        if form.is_valid():
            return base_view(request)
    return render(request,'employee.html',{'form':form})