# Generated by Django 3.0.7 on 2020-08-23 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabajos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trabajo',
            options={'ordering': ['estado'], 'verbose_name': 'Trabajo', 'verbose_name_plural': 'Trabajos'},
        ),
    ]