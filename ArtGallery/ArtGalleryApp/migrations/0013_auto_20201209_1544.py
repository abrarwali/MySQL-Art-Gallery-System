# Generated by Django 3.1.4 on 2020-12-09 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtGalleryApp', '0012_auto_20201208_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistaddress',
            name='Artist_ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artist_addresses', to='ArtGalleryApp.artist'),
        ),
    ]