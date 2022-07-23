from django.shortcuts import render
from .models import *
from .forms import *
from admins.models import FertilizerStock, SeedStock, FamersFeedback
from employee.models import SoilTestReports
import datetime
import calendar

# Create your views here.


def feedback(request):
    farmer_user_id = request.session['farmer_user_id']
    farmer = FarmerRegistrationModel.objects.get(user_id=farmer_user_id)
    if request.method == 'POST':
        feedback_name = request.POST.get('feedback_name')
        feedback_desc = request.POST.get('feedback_desc')
        farmer_name = farmer.name
        farmer_user_id = farmer.user_id
        try:
            model = FamersFeedback(feedback_name=feedback_name,
                                   feedback_desc=feedback_desc,
                                   farmer_name=farmer_name,
                                   farmer_user_id=farmer_user_id,
                                   )
            model.save()
            return render(request, 'farmer/farmer_home.html', {'farmer': farmer, 'feedback': 'feedback'})

        except Exception as e:
            return render(request, 'farmer/feedback.html', {'error': e})
    else:
        return render(request, 'farmer/feedback.html', {'farmer': farmer})


def soil_test_slot_booking(request):
    date = datetime.datetime.now()
    farmer_user_id = request.session['farmer_user_id']
    farmer = FarmerRegistrationModel.objects.get(user_id=farmer_user_id)
    initial_data = {'name': farmer.name, 'user_id': farmer.user_id,
                    'mobile_no': farmer.mobile_no, 'address': farmer.address, 'date': date}
    form = SoilTestSlotBookingForm(initial=initial_data)
    if request.method == "POST":

        form = SoilTestSlotBookingForm(initial=initial_data)
        try:
            form = SoilTestSlotBookingForm(request.POST)
            tracking_id = request.POST.get('tracking_id')
            if form.is_valid():
                form.save()
                return render(request, 'farmer/farmer_home.html', {'farmer': farmer, 'tracking_id': tracking_id})
        except Exception as e:
            return render(request, 'farmer/soil_test_slot_booking.html', {'farmer': farmer, 'form': form, 'exception': e})

    return render(request, 'farmer/soil_test_slot_booking.html', {'farmer': farmer, 'form': form})


def soil_test_tracking(request):
    farmer_user_id = request.session['farmer_user_id']
    farmer = FarmerRegistrationModel.objects.get(user_id=farmer_user_id)

    if request.method == "POST":
        tracking_id = request.POST.get('tracking_id')
        try:
            soil_test_tracking = SoilTestSlotBookingModel.objects.get(
                tracking_id=tracking_id)
            day = calendar.day_name[soil_test_tracking.date.weekday()]

            # check processed or not
            if soil_test_tracking.status == 'processed':
                processed_at = soil_test_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
            else:
                processed_at = None

            if soil_test_tracking.status == 'accepted':
                processed_at = soil_test_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                accepted_at = soil_test_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
            else:
                accepted_at = None

            if soil_test_tracking.status == 'slotAlloted':
                processed_at = soil_test_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                accepted_at = soil_test_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
                slotAlloted_at = soil_test_tracking.date + \
                    datetime.timedelta(hours=24, minutes=15)
            else:
                slotAlloted_at = None

            if soil_test_tracking.status == 'result':
                processed_at = soil_test_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                accepted_at = soil_test_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
                slotAlloted_at = soil_test_tracking.date + \
                    datetime.timedelta(hours=24, minutes=15)
                result_at = soil_test_tracking.date + \
                    datetime.timedelta(hours=30, minutes=30)
            else:
                result_at = None

            context = {
                'result_at': result_at,
                'slotAlloted_at': slotAlloted_at,
                'accepted_at': accepted_at,
                'processed_at': processed_at,
                'soil_test_tracking': soil_test_tracking,
                'day': day
            }
            try:
                test_report = SoilTestReports.objects.filter(
                    tracking_id=tracking_id)
                if test_report:
                    test_report = test_report.last().test_reports
                else:
                    test_report = None
            except Exception as e:
                print(e)
                return render(request, 'farmer/soil_test_tracking.html', {'farmer': farmer, 'tracking_id': tracking_id, 'error': e})
            return render(request, 'farmer/soil_test_tracking.html',  {'farmer': farmer, 'context': context, 'test_report': test_report})
        except Exception as e:
            return render(request, 'farmer/soil_test_tracking.html', {'farmer': farmer, 'tracking_id': tracking_id, 'error': e})
    else:
        return render(request, 'farmer/soil_test_tracking.html', {'farmer': farmer})


def seeds_ordering(request):
    date = datetime.datetime.now()
    farmer_user_id = request.session['farmer_user_id']
    farmer = FarmerRegistrationModel.objects.get(user_id=farmer_user_id)
    initial_data = {'name': farmer.name, 'user_id': farmer.user_id,
                    'mobile_no': farmer.mobile_no, 'address': farmer.address, 'date': date}
    form = SeedsOrderingForm(initial=initial_data)
    if request.method == "POST":
        try:
            form = SeedsOrderingForm(request.POST)
            tracking_id = request.POST.get('tracking_id')
            no_of_units = request.POST.get('no_of_packets')
            seed_type = request.POST.get('seed_type')
            if form.is_valid():
                seed_stock = SeedStock.objects.get(seed_type=seed_type)
                seed_stock.stock_units = seed_stock.stock_units - \
                    int(no_of_units)
                seed_stock.save()
                form.save()
                return render(request, 'farmer/farmer_home.html', {'farmer': farmer, 'tracking_id': tracking_id})
        except Exception as e:
            return render(request, 'farmer/seeds_ordering.html', {'farmer': farmer, 'form': form, 'exception': e})
    else:
        return render(request, 'farmer/seeds_ordering.html', {'farmer': farmer, 'form': form})


def seeds_order_tracking(request):
    farmer_user_id = request.session['farmer_user_id']
    farmer = FarmerRegistrationModel.objects.get(user_id=farmer_user_id)
    if request.method == "POST":
        tracking_id = request.POST.get('tracking_id')
        try:
            seeds_order_tracking = SeedsOrderingModel.objects.get(
                user_id=farmer_user_id, tracking_id=tracking_id)
            # status checking
            if seeds_order_tracking.status == 'processed':
                processed_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
            else:
                processed_at = None

            if seeds_order_tracking.status == 'pickedUp':
                processed_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                pickedUp_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
            else:
                pickedUp_at = None

            if seeds_order_tracking.status == 'shipped':
                processed_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                pickedUp_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
                shipped_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=24, minutes=15)
            else:
                shipped_at = None

            if seeds_order_tracking.status == 'outOfDelivery':
                processed_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                pickedUp_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
                shipped_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=24, minutes=15)
                outOfDelivery_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=30, minutes=30)
            else:
                outOfDelivery_at = None

            if seeds_order_tracking.status == 'delivered':
                processed_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                pickedUp_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
                shipped_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=24, minutes=15)
                outOfDelivery_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=30, minutes=30)
                delivered_at = seeds_order_tracking.date + \
                    datetime.timedelta(hours=36, minutes=50)
            else:
                delivered_at = None

            context = {
                'processed_at': processed_at,
                'pickedUp_at': pickedUp_at,
                'shipped_at': shipped_at,
                'outOfDelivery_at': outOfDelivery_at,
                'delivered_at': delivered_at,
                'seeds_order_tracking': seeds_order_tracking
            }

            return render(request, 'farmer/seeds_order_tracking.html', {'farmer': farmer, 'context': context})
        except Exception as e:
            return render(request, 'farmer/seeds_order_tracking.html', {'farmer': farmer, 'tracking_id': tracking_id, 'error': e})

    else:
        return render(request, 'farmer/seeds_order_tracking.html', {'farmer': farmer})


def ordering_fertilizers(request):
    date = datetime.datetime.now()
    farmer_user_id = request.session['farmer_user_id']
    farmer = FarmerRegistrationModel.objects.get(user_id=farmer_user_id)
    initial_data = {'name': farmer.name, 'user_id': farmer.user_id,
                    'mobile_no': farmer.mobile_no, 'address': farmer.address, 'date': date}
    form = FertilizersOrderingForm(initial=initial_data)
    if request.method == "POST":
        try:
            form = FertilizersOrderingForm(request.POST)
            tracking_id = request.POST.get('tracking_id')
            no_of_units = request.POST.get('no_of_packets')
            fertilizer_type = request.POST.get('fertilizer_type')
            if form.is_valid():
                fertilizer_stock = FertilizerStock.objects.get(
                    fertilizer_type=fertilizer_type)
                fertilizer_stock.stock_units = fertilizer_stock.stock_units - \
                    int(no_of_units)
                fertilizer_stock.save()
                form.save()
                return render(request, 'farmer/farmer_home.html', {'farmer': farmer, 'tracking_id': tracking_id})
        except Exception as e:

            return render(request, 'farmer/ordering_fertilizers.html', {'farmer': farmer, 'form': form, 'exception': e})
    else:
        return render(request, 'farmer/ordering_fertilizers.html', {'farmer': farmer, 'form': form})

    # return render(request, 'farmer/ordering_fertilizers.html')


def fertilizers_tracking(request):
    farmer_user_id = request.session['farmer_user_id']
    farmer = FarmerRegistrationModel.objects.get(user_id=farmer_user_id)
    if request.method == "POST":
        tracking_id = request.POST.get('tracking_id')
        try:
            fertilizers_tracking = FertilizersOrderingModel.objects.get(
                user_id=farmer_user_id, tracking_id=tracking_id)
            # status checking
            if fertilizers_tracking.status == 'processed':
                processed_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
            else:
                processed_at = None

            if fertilizers_tracking.status == 'pickedUp':
                processed_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                pickedUp_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
            else:
                pickedUp_at = None

            if fertilizers_tracking.status == 'shipped':
                processed_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                pickedUp_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
                shipped_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=24, minutes=15)
            else:
                shipped_at = None

            if fertilizers_tracking.status == 'outOfDelivery':
                processed_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                pickedUp_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
                shipped_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=24, minutes=15)
                outOfDelivery_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=30, minutes=30)
            else:
                outOfDelivery_at = None

            if fertilizers_tracking.status == 'delivered':
                processed_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=2, minutes=25)
                pickedUp_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=10, minutes=30)
                shipped_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=24, minutes=15)
                outOfDelivery_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=30, minutes=30)
                delivered_at = fertilizers_tracking.date + \
                    datetime.timedelta(hours=36, minutes=50)
            else:
                delivered_at = None

            context = {
                'processed_at': processed_at,
                'pickedUp_at': pickedUp_at,
                'shipped_at': shipped_at,
                'outOfDelivery_at': outOfDelivery_at,
                'delivered_at': delivered_at,
                'fertilizers_tracking': fertilizers_tracking
            }
            return render(request, 'farmer/fertilizers_tracking.html', {'farmer': farmer, 'context': context})
        except Exception as e:
            return render(request, 'farmer/fertilizers_tracking.html',  {'farmer': farmer, 'tracking_id': tracking_id, 'e': e})

    else:
        return render(request, 'farmer/fertilizers_tracking.html', {'farmer': farmer})
