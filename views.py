from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from .models import *
from demoapp.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
f



#task1 using foreign key
def salary_list(request):
    salary_list = EmployeeSalary.objects.all()
    s = {'salary_list':salary_list}
    return render(request,'salary.html',s)

def deletesalary(request,id):
    salary = EmployeeSalary.objects.get(id=id)
    salary.delete()
    return redirect('salary_list')

def update_salary(request,id):
    employee_list = EmployeeSalary.objects.get(id=id)
    emp_list = Employee.objects.all()
    if request.method == 'POST':
        basic_ = request.POST.get('basic')
        hra_ = request.POST.get('hra')
        special_allowance_ = request.POST.get('special_allowance')
        pf_deduction_ = request.POST.get('pf_deduction')
        income_tax_ = request.POST.get('income_tax')
        proffesional_tax_ = request.POST.get('proffesional_tax')
        convenience_ = request.POST.get('convenience')
        lta_ = request.POST.get('lta')
        employee_ = request.POST.get('employee')
        employee_list.basic = basic_
        employee_list.hra = hra_
        employee_list.special_allowance = special_allowance_
        employee_list.pf_deduction = pf_deduction_
        employee_list.income_tax = income_tax_
        employee_list.proffesional_tax = proffesional_tax_
        employee_list.convenience = convenience_
        employee_list.lta = lta_
        em_name = Employee.objects.get(id = int(employee_))
        employee_list.employee = em_name
        employee_list.save()
        return redirect('salary_list')
    else:
        a = {'salary':employee_list, 'employee_list': emp_list }
        return render(request,'update1.html',a)

def addcontent(request):
    employee_list = Employee.objects.all()
    if request.method == 'POST':
        basic_ = request.POST.get('basic')
        hra_ = request.POST.get('hra')
        special_allowance_ = request.POST.get('special_allowance')
        pf_deduction_ = request.POST.get('pf_deduction')
        income_tax_ = request.POST.get('income_tax')
        proffesional_tax_ = request.POST.get('proffesional_tax')
        convenience_ = request.POST.get('convenience')
        lta_ = request.POST.get('lta')
        employee = request.POST.get('employee')
        EmployeeSalary.objects.create(basic=basic_, hra=hra_, 
        special_allowance=special_allowance_, pf_deduction=pf_deduction_, 
        income_tax=income_tax_, proffesional_tax=proffesional_tax_, convenience=convenience_, 
        lta=lta_,employee_id=employee)
        return redirect('salary_list')
    else:
        return render(request,'update1.html',{'employee_list':employee_list})


 

    

    
       
