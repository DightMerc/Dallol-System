# Generated by Django 2.2.3 on 2019-10-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20191005_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinerieltor',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Активно'),
        ),
    ]
