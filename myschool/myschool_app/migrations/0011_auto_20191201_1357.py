# Generated by Django 2.2.7 on 2019-12-01 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
  dependencies = [
    ('myschool_app', '0010_auto_20191201_1355'),
  ]

  operations = [
    migrations.AlterField(
      model_name='avaliacao',
      name='teste',
      field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool_app.Teste', unique=True),
    ),
  ]
