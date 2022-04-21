# Generated by Django 3.2.8 on 2022-04-21 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('imagen', models.ImageField(null=True, upload_to='images/', verbose_name='Imagen')),
                ('descipcion', models.TextField(null=True, verbose_name='Descripcion')),
            ],
        ),
    ]
