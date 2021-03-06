# Generated by Django 3.0.6 on 2020-05-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200518_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='isClient',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courier',
            name='isCourier',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manager',
            name='isManager',
            field=models.BooleanField(default=False),
        ),
    ]
