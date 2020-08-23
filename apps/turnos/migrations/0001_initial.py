# Generated by Django 3.0.7 on 2020-08-23 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id_turno', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_turno', models.CharField(max_length=200, verbose_name='Tipo de turno')),
                ('fecha_turno', models.DateField(verbose_name='Fecha del turno')),
            ],
        ),
    ]
