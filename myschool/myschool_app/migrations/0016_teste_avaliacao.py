# Generated by Django 2.2.7 on 2019-12-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('myschool_app', '0015_auto_20191203_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='teste',
            name='avaliacao',
            field=models.FloatField(blank=True, null=True, verbose_name='Avaliação'),
        ),
    ]
