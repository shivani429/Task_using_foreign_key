from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from demoapp.views import *
urlpatterns = [

    # Employee Functions
    path('employee_list', views.employee_list, name='employee_list'),
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),
    path('edit_employee/<int:id>/', views.edit_employee, name='edit_employee'),
    path('add_employee/', views.add_employee, name='add_employee'),

    
    #task1 using foreign key
    path('salary',views.salary_list, name='salary_list'),
    path('deletesalary/<int:id>/', views.deletesalary, name='deletesalary'),
    path('update_salary/<int:id>/', views.update_salary, name='update_salary'),
    path('addcontent', views.addcontent, name='addcontent'),

]
