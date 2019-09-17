# Generated by Django 2.2.3 on 2019-09-01 12:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_onlinerieltor'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineRieltorTemporaryOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(max_length=10, verbose_name='Операция')),
                ('_property', models.CharField(max_length=30, verbose_name='Тип недвижимости')),
                ('title', models.TextField(verbose_name='Описание')),
                ('region', models.CharField(max_length=30, verbose_name='Район')),
                ('reference', models.CharField(max_length=30, verbose_name='Ориентир')),
                ('location_X', models.FloatField(verbose_name='Локация: широта')),
                ('location_Y', models.FloatField(verbose_name='Локация: долгота')),
                ('room_count', models.PositiveIntegerField(verbose_name='Количество комнат')),
                ('square', models.PositiveIntegerField(verbose_name='Общая площадь')),
                ('area', models.PositiveIntegerField(verbose_name='Количество соток')),
                ('state', models.CharField(max_length=30, verbose_name='Состояние')),
                ('ammount', models.CharField(max_length=255, verbose_name='Цена')),
                ('add_info', models.TextField(verbose_name='Инфо')),
                ('contact', models.PositiveIntegerField(verbose_name='Номер телефона')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('photo', models.ManyToManyField(to='api.Photo')),
                ('rieltor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.OnlineRieltor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TelegramUser')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineRieltorOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Актуально')),
                ('_type', models.CharField(max_length=10, verbose_name='Операция')),
                ('_property', models.CharField(max_length=30, verbose_name='Тип недвижимости')),
                ('title', models.TextField(verbose_name='Описание')),
                ('region', models.CharField(max_length=30, verbose_name='Район')),
                ('reference', models.CharField(max_length=30, verbose_name='Ориентир')),
                ('location_X', models.FloatField(verbose_name='Локация: широта')),
                ('location_Y', models.FloatField(verbose_name='Локация: долгота')),
                ('room_count', models.PositiveIntegerField(verbose_name='Количество комнат')),
                ('square', models.PositiveIntegerField(verbose_name='Общая площадь')),
                ('area', models.PositiveIntegerField(verbose_name='Количество соток')),
                ('state', models.CharField(max_length=30, verbose_name='Состояние')),
                ('ammount', models.CharField(max_length=255, verbose_name='Цена')),
                ('add_info', models.TextField(verbose_name='Инфо')),
                ('contact', models.PositiveIntegerField(verbose_name='Номер телефона')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('photo', models.ManyToManyField(to='api.Photo')),
                ('pro_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TemporaryOrder')),
                ('rieltor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.OnlineRieltor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TelegramUser')),
            ],
        ),
    ]