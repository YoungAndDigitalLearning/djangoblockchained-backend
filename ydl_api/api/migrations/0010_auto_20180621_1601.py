# Generated by Django 2.0.6 on 2018-06-21 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180621_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Post'),
        ),
    ]
