# Generated by Django 2.2.3 on 2019-09-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20190918_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ammount',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
    ]
