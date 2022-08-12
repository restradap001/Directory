from django import forms

from base.models import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'required': 'True','class': 'form-control'}),
            'type': forms.Select(attrs={'required': 'True', 'class': 'form-select'}),
            'address': forms.TextInput(attrs={'required': 'True','class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'required': 'True','class': 'form-control'}),
        }
