# Generated by Django 4.1.4 on 2022-12-20 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='cartao',
            field=models.CharField(max_length=200),
        ),
    ]