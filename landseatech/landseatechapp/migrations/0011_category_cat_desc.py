# Generated by Django 3.2.5 on 2021-12-16 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landseatechapp', '0010_rename_img_id_image_pdt_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_desc',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
