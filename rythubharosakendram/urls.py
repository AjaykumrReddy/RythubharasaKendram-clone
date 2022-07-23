"""rythubharosakendram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from farmers import views as farmerViews
from employee import views as employeeViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('farmer_register/', views.farmer_register, name='farmer_register'),
    path('employee_register/', views.employee_register, name='employee_register'),
    path('farmer_login/', views.farmer_login, name='farmer_login'),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('farmer_home/', views.farmer_home, name='former_home'),
    path('employee_home/', views.employee_home, name='employee_home'),

    # farmer Views
    path('feedback/', farmerViews.feedback, name='feedback'),
    path('soil_test_slot_booking/', farmerViews.soil_test_slot_booking,
         name='soil_test_slot_booking'),
    path('soil_test_tracking/', farmerViews.soil_test_tracking,
         name='soil_test_tracking'),
    path('seeds_ordering/', farmerViews.seeds_ordering,
         name='seeds_ordering'),
    path('seeds_order_tracking/', farmerViews.seeds_order_tracking,
         name='seeds_order_tracking'),
    path('ordering_fertilizers/', farmerViews.ordering_fertilizers,
         name='ordering_fertilizers'),
    path('fertilizers_tracking/', farmerViews.fertilizers_tracking,
         name='fertilizers_tracking'),

    # employee views
    path('employee_tasks/', employeeViews.employee_tasks, name='employee_tasks'),
    path('employee_performance/', employeeViews.employee_performance,
         name='employee_performance'),
    path('fertilizer_stock/', employeeViews.fertilizer_stock,
         name='fertilizer_stock'),
    path('seed_stock/', employeeViews.seed_stock, name='seed_stock'),
    path('soiltest_reports/', employeeViews.soiltest_reports,
         name='soiltest_reports'),
    path('submit_soiltest_report/', employeeViews.submit_soiltest_report,
         name='submit_soiltest_report'),

]
