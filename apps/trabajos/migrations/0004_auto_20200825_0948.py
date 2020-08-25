# Generated by Django 3.0.7 on 2020-08-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajos', '0003_presupuesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='Observaciones',
            field=models.CharField(default='', max_length=300, verbose_name='Observaciones'),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='Precio',
            field=models.IntegerField(default=0, verbose_name='Precio del servicio'),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='tipo_servicio',
            field=models.CharField(default='', max_length=220, verbose_name='Tipo de servicio'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='detalles',
            field=models.CharField(default='', max_length=200, verbose_name='Detalles'),
        ),
    ]
