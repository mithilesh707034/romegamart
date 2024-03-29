# Generated by Django 3.2.20 on 2024-03-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('slug', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('maincategory', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('maincategory_slug', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('category_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('category_slug', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Maincategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('slug', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='uploads')),
            ],
        ),
    ]
