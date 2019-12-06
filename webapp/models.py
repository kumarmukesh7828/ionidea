from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Create your models here.
class Employees(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    birth_date=models.DateField(blank=True,null=True)
    first_name=models.CharField(max_length=14,null=True,blank=True)
    last_name=models.CharField(max_length=16,null=True,blank=True)
    gender_choices=(
        ('M','Male'),
        ('F','Female'),
    )
    gender=models.CharField(max_length=1,choices=gender_choices)
    hire_date=models.DateField(null=True,blank=True,auto_now_add=True)

    def __str__(self):
        return str(self.emp_no)


class departments(models.Model):
    dept_no=models.IntegerField(null=True,blank=True,primary_key=False)
    dept_name=models.CharField(max_length=40,null=True,blank=True,unique=True)

class dept_emp(models.Model):
    emp_no=models.ForeignKey(Employees,blank=True,null=True,on_delete=models.CASCADE)
    dept_no=models.ForeignKey(departments,on_delete=models.CASCADE,null=True,blank=True)
    from_date=models.DateField(blank=True,null=True)
    to_date=models.DateField(blank=True,null=True)

class titles(models.Model):
    emp_no=models.ForeignKey(Employees,blank=True,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,null=True,blank=True)
    from_date=models.DateField(blank=True,null=True)
    to_date=models.DateField(blank=True,null=True)

class salaries(models.Model):
    emp_no=models.ForeignKey(Employees,blank=True,null=True,on_delete=models.CASCADE)
    salary=models.IntegerField(null=True,blank=True)
    from_date=models.DateField(null=True,blank=True)
    to_date=models.DateField(null=True,blank=True)



