# Generated by Django 3.2.8 on 2022-04-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='descipcion',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
    ]
