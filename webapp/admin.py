from django.contrib import admin
from webapp.models import Employees,salaries,dept_emp,departments,titles


# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['emp_no','birth_date','first_name','last_name']

class departmentsAdmin(admin.ModelAdmin):
    list_display = ['dept_no','dept_name']

class dept_empAdmin(admin.ModelAdmin):
    list_display = ['emp_no','dept_no','from_date','to_date']

class titlesAdmin(admin.ModelAdmin):
    list_display = ['emp_no','title','from_date','to_date']

class salariesAdmin(admin.ModelAdmin):
    list_display = ['emp_no','salary','from_date','to_date']

admin.site.register(Employees,EmployeesAdmin)
admin.site.register(departments,departmentsAdmin)
admin.site.register(dept_emp,dept_empAdmin)
admin.site.register(titles,titlesAdmin)
admin.site.register(salaries,salariesAdmin)
