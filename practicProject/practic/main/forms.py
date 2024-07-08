from .models import SearchReq
from django.forms import ModelForm, TextInput

class SearchReqForm(ModelForm):
    class Meta:
        model = SearchReq
        fields = ['position', 'exp', 'workForm', 'salary']


        widgets = {
            "position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность',
            }),
            "exp": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Опыт',
            }),
            "workForm": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Формат работы',
            }),
            "salary": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Зарплата',
            }),
        }