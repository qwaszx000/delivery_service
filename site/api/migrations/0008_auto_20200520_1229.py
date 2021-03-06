# Generated by Django 3.0.6 on 2020-05-20 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200519_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Surname',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='courier',
            name='Color',
            field=models.CharField(blank=True, default='#555555', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='courier',
            name='CoordinatesLatitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courier',
            name='CoordinatesLongtitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuisinetype',
            name='SecondName',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='Comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='Accompaniments',
            field=models.ManyToManyField(blank=True, to='api.Accompaniment'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='ImgMenuPage',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/img/menu_page/'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='ImgPopup',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/img/popup/'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='Modifications',
            field=models.ManyToManyField(blank=True, to='api.Modification'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='Packages',
            field=models.ManyToManyField(blank=True, to='api.Package'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='Tags',
            field=models.ManyToManyField(blank=True, to='api.DishTag'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='Toppings',
            field=models.ManyToManyField(blank=True, to='api.Topping'),
        ),
        migrations.AlterField(
            model_name='dishtag',
            name='SecondName',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='BattaryCharge',
            field=models.SmallIntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='modification',
            name='SecondName',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='CourierTakedMoney',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Courier'),
        ),
        migrations.AlterField(
            model_name='order',
            name='DeliveryAddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DeliveryAddress'),
        ),
        migrations.AlterField(
            model_name='order',
            name='PayInfo',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='PayType',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(default='new', max_length=128),
        ),
        migrations.AlterField(
            model_name='orderposition',
            name='Courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Courier'),
        ),
        migrations.AlterField(
            model_name='orderposition',
            name='Status',
            field=models.CharField(default='new', max_length=128),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='CoordinatesLatitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='CoordinatesLongtitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='MoreInfoEnglish',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='MoreInfoSecond',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='SectionMenus',
            field=models.ManyToManyField(blank=True, to='api.RestaurantSectionMenu'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='SeoSectionEnglish',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='SeoSectionSecond',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='SliderImgBigEng',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/img/eng/big/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='SliderImgBigSecond',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/img/second/big/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='SliderImgSmallEng',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/img/eng/small/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='SliderImgSmallSecond',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/img/second/small'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='Type',
            field=models.CharField(default='simple', max_length=12),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='TypesOfCusine',
            field=models.ManyToManyField(blank=True, to='api.CuisineType'),
        ),
        migrations.AlterField(
            model_name='restaurantsectionmenu',
            name='SecondName',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='taxe',
            name='SecondName',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Client')),
                ('Dishs', models.ManyToManyField(blank=True, to='api.Dish')),
            ],
        ),
    ]
