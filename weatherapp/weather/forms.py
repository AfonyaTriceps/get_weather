from django.forms import ModelForm, TextInput

from weather.models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ('name',)
        help_text = {'name': 'Enter the city'}
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'mt-3 form-control',
                    'name': 'city',
                    'id': 'city',
                    'placeholder': 'Input city',
                },
            ),
        }
