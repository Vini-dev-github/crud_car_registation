from django.forms import ModelForm
from app_registration.models import Cars

class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = ['modelo', 'marca', 'ano']
