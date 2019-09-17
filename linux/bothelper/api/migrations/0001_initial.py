# Generated by Django 2.2.2 on 2019-06-12 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=511, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'product type',
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveIntegerField(default=0, unique=True, verbose_name='Telegram ID')),
                ('full_name', models.CharField(default='', max_length=255, verbose_name='Name')),
                ('username', models.CharField(default='', max_length=255, null=True, verbose_name='Username')),
                ('phone', models.PositiveIntegerField(blank=True, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='')),
                ('price', models.PositiveIntegerField(default='0')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('products', models.ManyToManyField(to='api.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TelegramUser')),
            ],
        ),
    ]