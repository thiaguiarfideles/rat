# Generated by Django 3.0.6 on 2020-05-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rat_s', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospessoais',
            name='intervalo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Intervalo'),
        ),
    ]
