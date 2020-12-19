# Generated by Django 3.1.4 on 2020-12-07 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtGalleryApp', '0003_auto_20201206_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='Currency',
            field=models.CharField(choices=[('INR', 'Indian Rupee'), ('EUR', 'Euros'), ('USD', 'US Dollars')], default='INR', max_length=20),
        ),
    ]
