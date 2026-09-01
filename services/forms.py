from django import forms
from .models import ServiceRecord, WheelService, PartSale


class ServiceRecordForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_car_plate(self):
        data = self.cleaned_data['car_plate']
        return data.replace(" ", "").upper()


class WheelServiceForm(forms.ModelForm):
    class Meta:
        model = WheelService
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class PartSaleForm(forms.ModelForm):
    class Meta:
        model = PartSale
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
