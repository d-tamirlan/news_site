# Generated by Django 2.0.3 on 2018-10-30 16:50

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Заголовок')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(default='', max_length=100000, verbose_name='Текст')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Фото')),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='main.Category', verbose_name='Категория')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
