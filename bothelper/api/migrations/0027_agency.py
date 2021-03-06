# Generated by Django 2.2.3 on 2019-10-25 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0026_auto_20191016_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('active', models.BooleanField(default=False, verbose_name='Актуально')),
                ('rieltors', models.ManyToManyField(to='api.OnlineRieltor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
