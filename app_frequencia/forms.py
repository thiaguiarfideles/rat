

from django import forms
from app_frequencia.models import Frequencia
from django.contrib.auth.models import User


class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = '__all__'

