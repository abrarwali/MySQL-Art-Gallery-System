# Generated by Django 3.1.4 on 2020-12-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtGalleryApp', '0007_auto_20201207_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='Sold_In',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold_in_exhibition', to='ArtGalleryApp.exhibition'),
        ),
    ]