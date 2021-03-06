# Generated by Django 2.1 on 2019-12-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps_app', '0002_auto_20191207_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='hangouts_model',
            name='category',
            field=models.CharField(choices=[('cafe', 'Cafes'), ('bar', 'Bars'), ('gym', 'Gyms'), ('restaurant', 'Restaurants'), ('shopping_mall', 'Shopping Malls'), ('subway_station', 'Subway Stations')], default='cafe', max_length=50),
        ),
        migrations.AlterField(
            model_name='hangouts_model',
            name='add_1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hangouts_model',
            name='add_2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hangouts_model',
            name='add_3',
            field=models.CharField(max_length=50),
        ),
    ]
