# Generated by Django 4.2.8 on 2023-12-06 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
