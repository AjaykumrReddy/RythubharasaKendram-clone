from django import forms
from .models import *


class SoilTestSlotBookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['user_id'].widget.attrs['readonly'] = True
        # self.fields['mobile_no'].widget.attrs['readonly'] = True
        # self.fields['address'].widget.attrs['readonly'] = True
        self.fields['tracking_id'].widget.attrs['hidden'] = True
        self.fields['date'].widget.attrs['hidden'] = True
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = SoilTestSlotBookingModel
        fields = [
            'name',
            'user_id',
            'father_name',
            'survey_no',
            'mobile_no',
            'soil_type',
            'address',
            'tracking_id',
            'date'
        ]


class SeedsOrderingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['user_id'].widget.attrs['readonly'] = True
        # self.fields['mobile_no'].widget.attrs['readonly'] = True
        # self.fields['address'].widget.attrs['readonly'] = True
        self.fields['tracking_id'].widget.attrs['hidden'] = True
        self.fields['date'].widget.attrs['hidden'] = True
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = SeedsOrderingModel
        fields = [
            'name',
            'user_id',
            'father_name',
            'survey_no',
            'mobile_no',
            'seed_type',
            'no_of_packets',
            'address',
            'tracking_id',
            'date'
        ]


class FertilizersOrderingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['user_id'].widget.attrs['readonly'] = True
        # self.fields['mobile_no'].widget.attrs['readonly'] = True
        # self.fields['address'].widget.attrs['readonly'] = True
        self.fields['tracking_id'].widget.attrs['hidden'] = True
        self.fields['date'].widget.attrs['hidden'] = True
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = FertilizersOrderingModel
        fields = [
            'name',
            'user_id',
            'father_name',
            'survey_no',
            'mobile_no',
            'fertilizer_type',
            'no_of_packets',
            'address',
            'tracking_id',
            'date'
        ]
