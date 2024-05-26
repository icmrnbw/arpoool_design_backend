from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'phone', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите имя', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '+998', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'class': 'form-control'}),
        }
        labels = {
            'name': 'Ваше имя*',
            'phone': 'Ваш телефон*',
            'comment': 'Комментарий',
        }
