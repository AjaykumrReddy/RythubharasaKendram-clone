from django.contrib import admin

# Register your models here.
from .models import EmployeeRegistrationModel, SoilTestReports


class EmployeeRegistrationModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'emp_id',
        'password',
        'mobile_no',
        'mail',
        'aadhar_no',
        'address',
    ]


class SoilTestReportsAdmin(admin.ModelAdmin):
    list_display = (
        'emp_id',
        'tracking_id',
        'test_reports',
        'date'
    )


admin.site.register(EmployeeRegistrationModel, EmployeeRegistrationModelAdmin)
admin.site.register(SoilTestReports, SoilTestReportsAdmin)
