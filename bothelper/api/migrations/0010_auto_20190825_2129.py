# Generated by Django 2.2.3 on 2019-08-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_temporaryorder_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='media/', verbose_name='Фото'),
        ),
    ]
