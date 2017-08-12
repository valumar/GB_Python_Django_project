from django import forms
from main_app.models import MainService, Service


class MainServiceForm(forms.ModelForm):

    class Meta:
        model = MainService
        fields = ('name', 'description', 'fa_icon', 'bg_color')


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('name', 'description', 'category', 'price')
