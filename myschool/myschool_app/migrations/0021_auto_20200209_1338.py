# Generated by Django 3.0.3 on 2020-02-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool_app', '0020_auto_20191204_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_fim',
            field=models.DateField(verbose_name='Data de Fim'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateField(verbose_name='Data de Início'),
        ),
    ]
