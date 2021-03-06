# Generated by Django 2.1.1 on 2018-11-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelDetalhes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='titulo')),
                ('valor', models.FloatField(max_length=20, verbose_name='valor')),
                ('local', models.CharField(max_length=50, verbose_name='local')),
            ],
            options={
                'verbose_name': 'ModelDetalhes',
            },
        ),
        migrations.CreateModel(
            name='ModelEconomizou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(max_length=20, verbose_name='valor')),
            ],
            options={
                'verbose_name': 'ModelEconomizou',
            },
        ),
    ]
