# Generated by Django 3.1.7 on 2021-05-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oneteam_model',
            name='画像',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
