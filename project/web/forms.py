import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from core.models import Event, Gift


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'date_start', 'date_end', 'description', 'address', 'background', 'dresscode']
        widgets = {
            'date_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        date_start = self.cleaned_data.get('date_start')
        date_end = self.cleaned_data.get('date_end')
        if date_end <= date_start:
            self.add_error('date_end', ValidationError('Дата окончания события не может быть раньше даты начала.'))
        if timezone.now() >= date_end:
            self.add_error('date_end', ValidationError('Дата окончания события не может быть в прошлом.'))
        if timezone.now() >= date_start:
            self.add_error('date_start', ValidationError('Дата начала события не может быть в прошлом.'))

        return self.cleaned_data


class GiftForm(forms.ModelForm):

    class Meta:
        model = Gift
        fields = ['name', 'price', 'photo', 'link']