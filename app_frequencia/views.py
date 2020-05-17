# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app_frequencia.models import Frequencia
from app_frequencia.forms import FrequenciaForm
from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request,'app_frequencia/index.html')
    


def frequencia_view(request):
    form = FrequenciaForm()

    if request.method == 'POST':
        form = FrequenciaForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM')

    return render(request, 'app_frequencia/frequencia.html',{'form': form})