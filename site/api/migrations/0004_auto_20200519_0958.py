# Generated by Django 3.0.6 on 2020-05-19 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200519_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Phone',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Surname',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='courier',
            name='Color',
            field=models.CharField(default='#555555', max_length=7),
        ),
        migrations.AlterField(
            model_name='manager',
            name='BattaryCharge',
            field=models.SmallIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='manager',
            name='Restaurant',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Restaurant'),
        ),
    ]
