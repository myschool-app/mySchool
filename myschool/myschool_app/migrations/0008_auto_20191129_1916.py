# Generated by Django 2.2.7 on 2019-11-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
  dependencies = [
    ('myschool_app', '0007_auto_20191129_1901'),
  ]

  operations = [
    migrations.AlterField(
      model_name='teste',
      name='notas',
      field=models.TextField(blank=True, max_length=255, verbose_name='Notas'),
    ),
  ]
