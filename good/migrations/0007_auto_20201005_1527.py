# Generated by Django 3.1.1 on 2020-10-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0006_auto_20201005_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]
