# Generated by Django 2.2.3 on 2019-08-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_product_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='language',
            field=models.CharField(default='RU', max_length=5, verbose_name='Язык'),
        ),
    ]
