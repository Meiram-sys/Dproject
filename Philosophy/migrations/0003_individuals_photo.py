# Generated by Django 4.0.3 on 2022-03-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Philosophy', '0002_category_alter_philosophers_options_individuals'),
    ]

    operations = [
        migrations.AddField(
            model_name='individuals',
            name='photo',
            field=models.ImageField(null=True, upload_to='', verbose_name='Фото'),
        ),
    ]
