# Generated by Django 2.2.3 on 2019-09-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20190908_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinerieltororder',
            name='floor',
            field=models.PositiveIntegerField(default=1, verbose_name='Этаж квартиры'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onlinerieltororder',
            name='main_floor',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество этажей в доме'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onlinerieltortemporaryorder',
            name='floor',
            field=models.PositiveIntegerField(default=1, verbose_name='Этаж квартиры'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onlinerieltortemporaryorder',
            name='main_floor',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество этажей в доме'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='floor',
            field=models.PositiveIntegerField(default=1, verbose_name='Этаж квартиры'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='main_floor',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество этажей в доме'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temporaryorder',
            name='floor',
            field=models.PositiveIntegerField(default=1, verbose_name='Этаж квартиры'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temporaryorder',
            name='main_floor',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество этажей в доме'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='onlinerieltororder',
            name='area',
            field=models.FloatField(verbose_name='Количество соток'),
        ),
        migrations.AlterField(
            model_name='onlinerieltororder',
            name='square',
            field=models.FloatField(verbose_name='Общая площадь'),
        ),
        migrations.AlterField(
            model_name='onlinerieltortemporaryorder',
            name='area',
            field=models.FloatField(verbose_name='Количество соток'),
        ),
        migrations.AlterField(
            model_name='onlinerieltortemporaryorder',
            name='square',
            field=models.FloatField(verbose_name='Общая площадь'),
        ),
        migrations.AlterField(
            model_name='order',
            name='area',
            field=models.FloatField(verbose_name='Количество соток'),
        ),
        migrations.AlterField(
            model_name='order',
            name='square',
            field=models.FloatField(verbose_name='Общая площадь'),
        ),
        migrations.AlterField(
            model_name='temporaryorder',
            name='area',
            field=models.FloatField(verbose_name='Количество соток'),
        ),
        migrations.AlterField(
            model_name='temporaryorder',
            name='square',
            field=models.FloatField(verbose_name='Общая площадь'),
        ),
    ]
