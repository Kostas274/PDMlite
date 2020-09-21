# Generated by Django 3.1.1 on 2020-09-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_number', models.CharField(db_index=True, max_length=30, verbose_name='doc_number')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('published_date', models.DateField(verbose_name='published_date')),
                ('image', models.ImageField(upload_to='certificates')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ['name'],
            },
        ),
    ]
