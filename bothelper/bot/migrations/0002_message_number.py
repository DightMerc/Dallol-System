# Generated by Django 2.2.2 on 2019-06-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
