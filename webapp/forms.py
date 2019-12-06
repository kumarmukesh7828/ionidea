from django import forms
from webapp.models import Employees,salaries,departments,dept_emp,titles
from webapp.admin import EmployeesAdmin,salariesAdmin,dept_empAdmin,departmentsAdmin,titlesAdmin

class EmployeesForm(forms.ModelForm):
    class Meta:
        model= Employees
        fields='__all__'


class departmentsForm(forms.ModelForm):
    class Meta:
        model=departments
        fields='__all__'

class dept_empForm(forms.ModelForm):
    class Meta:
        model=dept_emp
        fields='__all__'

class titlesForm(forms.ModelForm):
    class Meta:
        model=titles
        fields='__all__'

class salariesForm(forms.ModelForm):
    class Meta:
        model=salaries
        fields='__all__'