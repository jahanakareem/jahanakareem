# Generated by Django 3.2.5 on 2022-02-03 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landseatechapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('blogcat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landseatechapp.blogcategory')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
