# Generated by Django 4.2.3 on 2023-07-25 16:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_create_date_commment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commment',
            name='created_dt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
