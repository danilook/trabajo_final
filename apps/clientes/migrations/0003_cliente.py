# Generated by Django 3.0.7 on 2020-08-21 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200816_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='clientes.Persona')),
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('clientes.persona',),
        ),
    ]
