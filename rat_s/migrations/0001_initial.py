# Generated by Django 3.0.6 on 2020-05-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosPessoais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_profissional', models.CharField(default='', max_length=50, verbose_name='Nome Profissional')),
                ('nm_empresa', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome Empresa')),
                ('nm_cliente', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome Cliente')),
                ('nm_contato', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contato Contratante')),
                ('tel_contato', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefone Contato')),
                ('dt_atendimento', models.DateTimeField(blank=True, null=True, verbose_name='Data do atendimento')),
                ('intervalo', models.CharField(blank=True, choices=[('Primeiro:', '1 HORA'), ('Segundo:', '2 HORAS'), ('Terceiro:', '30 MIN'), ('Quarto:', '45 MIN'), ('NORMAL', 'OUTROS VALORES')], max_length=100, null=True, verbose_name='Intervalo')),
                ('dt_fim_atendimento', models.DateTimeField(blank=True, null=True, verbose_name='Data fim do atendimento')),
                ('servico_contratado', models.TextField(blank=True, null=True, verbose_name='Servico_contratado')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('cidade', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cidade')),
                ('ds_endereco', models.CharField(blank=True, max_length=200, null=True, verbose_name='Endereço')),
                ('deslocamento_ida', models.CharField(blank=True, max_length=200, null=True, verbose_name='Deslocamento ida')),
                ('deslocamento_volta', models.CharField(blank=True, max_length=200, null=True, verbose_name='Deslocamento volta')),
                ('comentarios', models.TextField(blank=True, null=True, verbose_name='Comentarios')),
                ('upload', models.FileField(blank=True, null=True, upload_to='images/')),
                ('data_insercao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
