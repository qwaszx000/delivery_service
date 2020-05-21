# Generated by Django 3.0.6 on 2020-05-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200519_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='CoordinatesLatitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='CoordinatesLongtitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='courier',
            name='Color',
            field=models.CharField(default='#555555', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='BattaryCharge',
            field=models.SmallIntegerField(default=100, null=True),
        ),
    ]