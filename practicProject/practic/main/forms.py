from .models import SearchReq
from django.forms import ModelForm, TextInput, Select, CheckboxInput, CharField
from django import forms

class SearchReqForm(ModelForm):
    workForm = forms.BooleanField(required=False, initial='fullDay')
    workForm1 = forms.BooleanField(required=False, initial='shift')
    workForm2 = forms.BooleanField(required=False, initial='flexible')
    workForm3 = forms.BooleanField(required=False, initial='remote')
    workForm4 = forms.BooleanField(required=False, initial='flyInFlyOut')
    slider = forms.IntegerField(
        min_value=30000,
        max_value=300000,
        step_size=1000,
        widget=forms.NumberInput(attrs={'type': 'range', 'id': 'salary-slider'})
    )
    class Meta:
        model = SearchReq

        fields = ['position', 'exp', 'workForm','workForm1','workForm2','workForm3','workForm4','slider']

        exp = (
            ('noExperience', 'Нет опыта'),
            ('between1And3', 'От 1 года до 3 лет'),
            ('between3And6', 'От 3 до 6 лет'),
            ('moreThan6', 'Более 6 лет'),
        )




        widgets = {
            "position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность',
            }),
            "exp": Select(choices=exp,attrs={
                'class': 'form-select',
                'placeholder': 'Опыт',
            }),
            "workForm": CheckboxInput(attrs={
                'class': 'form-check-input',
                'value':  'fullDay',
            }),
            "workForm1": CheckboxInput(attrs={
                'class': 'form-check-input',
                'value': 'shift',
            }),
            "workForm2": CheckboxInput(attrs={
                'class': 'form-check-input',
                'value': 'flexible',
            }),
            "workForm3": CheckboxInput(attrs={
                'class': 'form-check-input',
                'value': 'remote',
            }),
            "workForm4": CheckboxInput(attrs={
                'class': 'form-check-input',
                'value': 'flyInFlyOut',
            }),
            # "salary": TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Зарплата',
            # }),
        }