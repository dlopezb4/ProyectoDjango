# Generated by Django 3.2.7 on 2021-09-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actualizacion', models.DateField(auto_created=True)),
                ('creacion', models.DateField(auto_created=True)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
    ]
