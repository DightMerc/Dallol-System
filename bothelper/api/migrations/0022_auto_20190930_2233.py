# Generated by Django 2.2.3 on 2019-09-30 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_commonrieltoruser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onlinerieltororder',
            old_name='_property',
            new_name='property',
        ),
        migrations.RenameField(
            model_name='onlinerieltororder',
            old_name='_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='onlinerieltortemporaryorder',
            old_name='_property',
            new_name='property',
        ),
        migrations.RenameField(
            model_name='onlinerieltortemporaryorder',
            old_name='_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='_property',
            new_name='property',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='temporaryorder',
            old_name='_property',
            new_name='property',
        ),
        migrations.RenameField(
            model_name='temporaryorder',
            old_name='_type',
            new_name='type',
        ),
    ]