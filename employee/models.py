from django.db import models

# Create your models here.


class EmployeeRegistrationModel(models.Model):
    name = models.CharField(max_length=120)
    emp_id = models.CharField(unique=True, max_length=120)
    password = models.CharField(max_length=120)
    mobile_no = models.CharField(max_length=120)
    mail = models.CharField(max_length=120, unique=True)
    aadhar_no = models.CharField(unique=True, max_length=120)
    address = models.CharField(max_length=120)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.emp_id

    class Meta:
        db_table = 'EmployeeRegistration'


class SoilTestReports(models.Model):
    emp_id = models.CharField(max_length=20)
    tracking_id = models.CharField(max_length=16)
    test_reports = models.FileField(upload_to='reports/')
    date = models.DateTimeField()
