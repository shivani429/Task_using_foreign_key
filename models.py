from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse


class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=30)
    ephn = models.IntegerField()
    esalary = models.IntegerField()

    def __str__(self):
        return str(self.ename)
   
     
class EmployeeSalary(models.Model):
    basic = models.CharField(max_length=30)
    hra = models.IntegerField()
    special_allowance = models.IntegerField()
    pf_deduction = models.IntegerField()
    income_tax = models.IntegerField()
    proffesional_tax = models.IntegerField()
    convenience = models.IntegerField()
    lta = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='EmployeeSalary',null=True, blank=True)

    def __str__(self):
        return str(self.basic)
   




    
