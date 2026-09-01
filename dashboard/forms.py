from django import forms
from .models import Service, WheelJob


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            # Adding Bootstrap 'form-control' class to all inputs
            'car_plate': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'price': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
