# Generated by Django 2.2.3 on 2019-08-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporaryorder',
            name='photo',
            field=models.ManyToManyField(to='api.Photo'),
        ),
    ]
