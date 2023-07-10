# Generated by Django 4.2.3 on 2023-07-10 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author_post_tags_alter_post_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='posts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 10, 16, 34, 34, 725720, tzinfo=datetime.timezone.utc)),
        ),
    ]