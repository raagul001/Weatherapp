from django.forms import ModelForm,TextInput
from .models import city

class world(ModelForm):
    class Meta:
        model=city
        fields=["name"]
        widgets={'name':TextInput(attrs={'class':'form-control','placeholder':'City Name'})}