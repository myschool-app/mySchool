# Generated by Django 2.2.7 on 2019-11-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('myschool_app', '0005_teste_notas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='notas',
            field=models.CharField(max_length=255, verbose_name='Notas'),
        ),
    ]
