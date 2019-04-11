from django.contrib import admin
from firstapp.models import Employee,Workhour,Salary,Login

# Register your models here.


admin.site.register(Employee)
admin.site.register(Workhour)
admin.site.register(Salary)
admin.site.register(Login)
