from django import forms
from datetime import datetime, time
from django.core.exceptions import ValidationError


class ReservationForm(forms.Form):

    username = forms.CharField(
        label=False,
        
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bg-transparent border-warning p-4',
                'placeholder': 'username',
                'required': 'required',
            }
        )
    )
    email = forms.EmailField(
        label=False,

        widget=forms.EmailInput(
            attrs={
                'class': 'form-control bg-transparent border-warning p-4',
                'placeholder': 'Email',
                'required': 'required',
            }
        )
    )
    date = forms.DateField(
            label=False,
            widget=forms.DateInput(
                attrs={
                    'class': 'form-control bg-transparent border-warning p-4',
                    'placeholder': 'Date',
                    'type': 'date',
                },
                format='%Y-%m-%d'
            )
        )
    time = forms.TimeField(
        label=False,
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control bg-transparent border-warning p-4 datetimepicker-input',
                'placeholder': 'Time',
                'data-target': '#time',
                'data-toggle': 'datetimepicker',
                'type': 'time',
            }
        )
    )
    personnes = forms.IntegerField(
        label=False,

        min_value=1,
        max_value=7,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control bg-transparent border-warning p-4',
                'placeholder': 'Person',
                'required': 'required',
            }
        )
    )
    type_reservation = forms.ChoiceField(
        label=False,

        choices=[
            ('table', 'Réserver Table'),
            ('etudiant', 'Réserver Espace des Etudiants'),
            ('billard', 'Réserver Table de Billard'),
        ],
        widget=forms.Select(
            attrs={
                'class': 'custom-select bg-transparent border-warning px-4',
                'style': 'height: 49px;',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        current_user = self.request.user

        selected_date = cleaned_data.get('date')
        selected_time = cleaned_data.get('time')

        current_date = datetime.now().date()
        current_time = datetime.now().time()

        if selected_date < current_date:
            raise forms.ValidationError('Selected date is in the past.')

        if selected_date == current_date and selected_time < current_time:
            raise forms.ValidationError('Selected time is in the past.')

        if username != current_user.username or email != current_user.email:
            raise forms.ValidationError('Invalid username or email.')

        return cleaned_data
    def clean_time(self):
        time_value = self.cleaned_data['time']
        date_value = self.cleaned_data['date']

        is_weekend = date_value.weekday() >= 5

        if is_weekend:
            start_time = time(8, 0)  
            end_time = time(18, 0)  
        else:
            start_time = time(7, 30)  
            end_time = time(17, 30)  

        if not start_time <= time_value <= end_time:
            raise forms.ValidationError('L\'heure de réservation est en dehors de la plage autorisée.')

        return time_value
