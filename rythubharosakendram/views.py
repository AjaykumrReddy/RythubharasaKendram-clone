from django.shortcuts import render
from farmers.models import FarmerRegistrationModel
from employee.models import EmployeeRegistrationModel

# Create your views here.


def index(request):
    return render(request, 'index.html')


def farmer_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        mobile_no = request.POST.get('mobile_no')
        aadhar_no = request.POST.get('aadhar_no')
        address = request.POST.get('address')
        try:
            model = FarmerRegistrationModel(
                name=name,
                user_id=user_id,
                password=password,
                mobile_no=mobile_no,
                aadhar_no=aadhar_no,
                address=address,
            )
            model.save()
            return render(request, 'farmer_register.html', {'success': 'Registerd Successfully'})
        except Exception as e:
            return render(request, 'farmer_register.html', {'error': e})
    else:
        return render(request, 'farmer_register.html')


def employee_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        emp_id = request.POST.get('emp_id')
        password = request.POST.get('password')
        mobile_no = request.POST.get('mobile_no')
        mail = request.POST.get('mail')
        aadhar_no = request.POST.get('aadhar_no')
        address = request.POST.get('address')
        try:
            model = EmployeeRegistrationModel(
                name=name,
                emp_id=emp_id,
                password=password,
                mobile_no=mobile_no,
                mail=mail,
                aadhar_no=aadhar_no,
                address=address
            )
            model.save()
            return render(request, 'employee_register.html', {'success': 'Registerd Successfully'})
        except Exception as e:
            return render(request, 'employee_register.html', {'error': e})
    else:
        return render(request, 'employee_register.html')


def farmer_login(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        try:
            print(f"Login {user_id} password {password}")
            farmer = FarmerRegistrationModel.objects.get(
                user_id=user_id, password=password)
            request.session['farmer_user_id'] = user_id
            return render(request, 'farmer/farmer_home.html', {'farmer': farmer})
        except Exception as e:
            print(e)
            return render(request, 'farmer_login.html', {'msg': e})
    else:
        return render(request, 'farmer_login.html')


def employee_login(request):
    if request.method == "POST":
        emp_id = request.POST.get('emp_id')
        password = request.POST.get('password')
        try:
            employee = EmployeeRegistrationModel.objects.get(
                emp_id=emp_id, password=password)
            if employee.status:
                request.session['employee_emp_id'] = emp_id
                return render(request, 'employee/employee_home.html', {'employee': employee})
            else:
                return render(request, 'employee_login.html', {'msg': 'Your account not yet activated'})
        except Exception as e:
            return render(request, 'employee_login.html', {'msg': e})
    else:
        return render(request, 'employee_login.html')


def farmer_home(request):
    farmer_user_id = request.session['farmer_user_id']
    farmer = FarmerRegistrationModel.objects.get(user_id=farmer_user_id)
    return render(request, 'farmer/farmer_home.html', {'farmer': farmer})


def employee_home(request):
    emp_id = request.session['employee_emp_id']
    employee = EmployeeRegistrationModel.objects.get(emp_id=emp_id)
    return render(request, 'employee/employee_home.html', {'employee': employee})
