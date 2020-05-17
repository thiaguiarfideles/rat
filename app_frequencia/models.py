# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import socket

class ConfiguracaoHora(models.Model):
    descricao_hora = models.CharField('Descrição de configuração da hora', max_length = 128)
    hora_entrada_1 = models.TimeField('Hora de entrada 1', blank = True, null = True)
    hora_saida_1 = models.TimeField('Hora de saída 1', blank = True, null = True)
    hora_entrada_2 = models.TimeField('Hora de entrada 2', blank = True, null = True)
    hora_saida_2 = models.TimeField('Hora de saída 2', blank = True, null = True)

    def __str__(self):
        return self.descricao_hora

class Cargo(models.Model):
    descricao_cargo = models.CharField('Descrição do cargo', max_length = 128)

    def __str__(self):
        return self.descricao_cargo

class Funcionario(models.Model):
    nome = models.CharField('Nome do funcionário', max_length = 128)
    usuario = models.OneToOneField(User, on_delete = models.SET_NULL, blank = True, null = True, verbose_name = 'Usuário')
    funcionario_pessoa = models.ForeignKey('Funcionario', on_delete = models.SET_NULL, blank = True, null = True)
    cargo = models.ForeignKey(Cargo, on_delete = models.SET_NULL, blank = True, null = True, verbose_name = 'Cargo do funcionário')
    configuracao_hora = models.ForeignKey(ConfiguracaoHora, on_delete = models.SET_NULL, blank = True, null = True, verbose_name = 'Configuração da hora')

    def __str__(self):
        return self.nome

class TipoBatidaPonto(models.Model):
    descricao_ponto = models.CharField('Descrição da batida de ponto', max_length = 128)

    def __str__(self):
        return self.descricao_ponto

class StatusPonto(models.Model):
    descricao_status = models.CharField('Descrição do status do ponto', max_length = 128)

    def __str__(self):
        return self.descricao_status


def pegar_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

class Frequencia(models.Model):
    hora_ponto = models.TimeField('Hora de entrada 1', blank=True, null=True)
    hora_saida_ponto = models.TimeField('Hora da saida 1', blank=True, null=True)
    ip_registro =  models.CharField(max_length = 20, default = pegar_ip(), editable = False, blank = True, null = True)
    data_resgistro = models.DateField('Data do registro', auto_now_add = True, blank = True, null = True)
    juntificativa = models.TextField(blank = True, null = True)
    tipo_ponto = models.ForeignKey(TipoBatidaPonto, on_delete = models.SET_NULL, blank = True, null = True, verbose_name  = 'Tipo ponto')
    status_ponto = models.ForeignKey(StatusPonto, on_delete = models.SET_NULL, blank = True, null = True, verbose_name = 'Status ponto')
    funcionario = models.ForeignKey(Funcionario, on_delete = models.SET_NULL, blank = True, null = True, verbose_name = 'Funcionário')


    def __str__(self):
        return 'Frequencia '+ str(self.funcionario) + ' '+ str(self.data_resgistro)
    
