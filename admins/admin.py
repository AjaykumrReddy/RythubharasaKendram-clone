from django.contrib import admin
from .models import *

# Register your models here.


class EmplyoyeeDailyTaskadmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'desc'
    )


class FertilizerStockAdmin(admin.ModelAdmin):
    list_display = (
        'fertilizer_type',
        'stock_units'
    )


class SeedStockAdmin(admin.ModelAdmin):
    list_display = (
        'seed_type',
        'stock_units'
    )


class FamersFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'feedback_name',
        'feedback_desc',
        'farmer_name',
        'farmer_user_id'
    )


admin.site.register(EmplyoyeeDailyTask, EmplyoyeeDailyTaskadmin)
admin.site.register(FertilizerStock, FertilizerStockAdmin)
admin.site.register(SeedStock, SeedStockAdmin)
admin.site.register(FamersFeedback, FamersFeedbackAdmin)
