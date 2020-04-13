# Generated by Django 2.2.7 on 2019-12-01 13:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myschool_app', '0008_auto_20191129_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teste',
            name='avaliacao',
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.FloatField(verbose_name='Avaliação')),
                ('notas', models.TextField(max_length=255, verbose_name='Notas')),
                ('teste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool_app.Teste')),
                ('utilizador',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliação',
            },
        ),
    ]
