# Generated by Django 2.2.2 on 2019-06-12 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20190611_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='locale',
        ),
        migrations.DeleteModel(
            name='Locale',
        ),
    ]
