# Generated by Django 3.1.4 on 2020-12-07 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtGalleryApp', '0008_buy_sold_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='Sold_In',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold_in_exhibition', to='ArtGalleryApp.exhibition'),
        ),
    ]
