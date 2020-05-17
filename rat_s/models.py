from django.db import models
from django.contrib.auth.models import User



# Create your models here.
STATUS_INTERVALO = (
    ('Primeiro:', '1 HORA'),
    ('Segundo:', '2 HORAS'),
    ('Terceiro:', '30 MIN'),
    ('Quarto:', '45 MIN'),
    ('NORMAL', 'OUTROS VALORES'),
    
)


class DadosPessoais(models.Model):

	nm_profissional = models.CharField(verbose_name="Nome Profissional", max_length=50, default='')
	nm_empresa = models.CharField(verbose_name="Nome Empresa", max_length=100, blank=True, null=True)
	nm_cliente = models.CharField(verbose_name="Nome Cliente", max_length=100, blank=True, null=True)
	nm_contato = models.CharField(verbose_name="Contato Contratante", max_length=100, blank=True, null=True)
	tel_contato = models.CharField(verbose_name="Telefone Contato", max_length=100, blank=True, null=True)
	dt_atendimento = models.DateTimeField(verbose_name="Data do atendimento", blank=True, null=True)
	intervalo = models.TimeField(verbose_name="Intervalo inicial", blank=True, null=True)
	dt_fim_atendimento = models.DateTimeField(verbose_name="Data fim do atendimento", blank=True, null=True)
	servico_contratado = models.TextField(blank=True, null=True,verbose_name="Servico_contratado")
	email = models.EmailField(verbose_name="Email", max_length=200, blank=True, null=True)
	cidade = models.CharField(verbose_name="Cidade", max_length=200, blank=True, null=True)
	ds_endereco = models.CharField(verbose_name="Endereço", max_length=200, blank=True, null=True)
	deslocamento_ida = models.CharField(verbose_name="Deslocamento ida", max_length=200, blank=True, null=True)
	deslocamento_volta = models.CharField(verbose_name="Deslocamento volta", max_length=200, blank=True, null=True)
	comentarios = models.TextField(blank=True, null=True,verbose_name="Comentarios")
	upload = models.FileField(blank=True, null=True, upload_to='images/')
	intervalo_inicial = models.TimeField(verbose_name="Intervalo final", blank=True, null=True)

	data_insercao = models.DateTimeField(auto_now_add=True)
	

    

	def __str__(self):
		return self.nm_profissional
    