# Generated by Django 3.2.20 on 2024-03-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_seller_follower'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='otp',
            field=models.IntegerField(blank=True, default=9241, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='verification',
            field=models.CharField(blank=True, default='Pending', max_length=100, null=True),
        ),
    ]
