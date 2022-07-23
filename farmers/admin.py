from django.contrib import admin
from . models import *

# Register your models here.


class FarmerRegistrationModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'user_id',
        'password',
        'mobile_no',
        'aadhar_no',
        'address',
    ]


class SoilTestSlotBookingModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'user_id',
        'father_name',
        'survey_no',
        'mobile_no',
        'soil_type',
        'address',
        'tracking_id',
        'date',
        'status'
    ]


class SeedsOrderingModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'user_id',
        'father_name',
        'survey_no',
        'mobile_no',
        'seed_type',
        'no_of_packets',
        'address',
        'tracking_id',
        'date',
        'status'
    ]


class FertilizersOrderingModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'user_id',
        'father_name',
        'survey_no',
        'mobile_no',
        'fertilizer_type',
        'no_of_packets',
        'address',
        'tracking_id',
        'date',
        'status'
    ]


admin.site.register(FarmerRegistrationModel, FarmerRegistrationModelAdmin)
admin.site.register(SoilTestSlotBookingModel, SoilTestSlotBookingModelAdmin)
admin.site.register(SeedsOrderingModel, SeedsOrderingModelAdmin)
admin.site.register(FertilizersOrderingModel, FertilizersOrderingModelAdmin)
