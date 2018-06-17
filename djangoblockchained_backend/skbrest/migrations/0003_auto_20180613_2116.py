# Generated by Django 2.0.6 on 2018-06-13 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skbrest', '0002_auto_20180612_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendarentry',
            options={'verbose_name': 'calendar entry', 'verbose_name_plural': 'calendar entries'},
        ),
        migrations.RemoveField(
            model_name='resource',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='ressources',
            field=models.ManyToManyField(to='skbrest.Resource'),
        ),
        migrations.AlterField(
            model_name='anouncement',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]