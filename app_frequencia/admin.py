# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ConfiguracaoHora, Cargo, Funcionario, StatusPonto, Frequencia, TipoBatidaPonto


@admin.register(ConfiguracaoHora)
class ConfiguracaoHoraAdmin(admin.ModelAdmin):
    pass


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass


@admin.register(StatusPonto)
class StatusPontoAdmin(admin.ModelAdmin):
    pass


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoBatidaPonto)
class TipoBatidaPontoAdmin(admin.ModelAdmin):
    pass

# Register your models here.
