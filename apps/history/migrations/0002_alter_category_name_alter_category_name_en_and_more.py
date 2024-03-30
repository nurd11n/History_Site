# Generated by Django 4.2.5 on 2024-03-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ky',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='slug',
            field=models.SlugField(blank=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title_ky',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='years',
            name='ages',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='years',
            name='slug',
            field=models.SlugField(blank=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
