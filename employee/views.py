from django.shortcuts import render
from employee.models import EmployeeRegistrationModel, SoilTestReports
from admins.models import EmplyoyeeDailyTask, FertilizerStock, SeedStock
from farmers.models import SoilTestSlotBookingModel
import datetime
# Create your views here.


def employee_tasks(request):
    tasks = EmplyoyeeDailyTask.objects.all()
    emp_id = request.session['employee_emp_id']
    employee = EmployeeRegistrationModel.objects.get(emp_id=emp_id)
    return render(request, 'employee/employee_tasks.html', {'tasks': tasks, 'employee': employee})


def employee_performance(request):
    emp_id = request.session['employee_emp_id']
    employee = EmployeeRegistrationModel.objects.get(emp_id=emp_id)
    return render(request, 'employee/employee_performance.html', {'employee': employee})


def fertilizer_stock(request):
    stocks = FertilizerStock.objects.all()
    emp_id = request.session['employee_emp_id']
    employee = EmployeeRegistrationModel.objects.get(emp_id=emp_id)
    return render(request, 'employee/fertilizer_stock.html', {'stocks': stocks, 'employee': employee})


def seed_stock(request):
    stocks = SeedStock.objects.all()
    emp_id = request.session['employee_emp_id']
    employee = EmployeeRegistrationModel.objects.get(emp_id=emp_id)
    return render(request, 'employee/seed_stock.html', {'stocks': stocks, 'employee': employee})


def soiltest_reports(request):
    emp_id = request.session['employee_emp_id']
    employee = EmployeeRegistrationModel.objects.get(emp_id=emp_id)
    soil_type = request.GET.get('soil_type')
    soiltest_requests = SoilTestSlotBookingModel.objects.filter(
        soil_type=soil_type)
    return render(request, 'employee/soiltest_reports.html', {'soiltest_requests': soiltest_requests, 'employee': employee})


def submit_soiltest_report(request):
    tracking_id = request.GET.get('tracking_id')
    emp_id = request.session['employee_emp_id']
    employee = EmployeeRegistrationModel.objects.get(emp_id=emp_id)
    soiltest_report = SoilTestSlotBookingModel.objects.get(
        tracking_id=tracking_id)
    if request.method == 'POST':
        test_report = request.FILES['test_report']
        date = datetime.datetime.now()
        try:
            soiltest_reports = SoilTestReports.objects.create(
                emp_id=emp_id,
                tracking_id=tracking_id,
                test_reports=test_report,
                date=date
            )
            soiltest_reports.save()
            return render(request, 'employee/employee_home.html', {'employee': employee})
        except Exception as e:
            return render(request, 'employee/submit_soiltest_report.html', {'error': e, 'employee': employee})

    else:
        return render(request, 'employee/submit_soiltest_report.html', {'soiltest_report': soiltest_report, 'employee': employee})
