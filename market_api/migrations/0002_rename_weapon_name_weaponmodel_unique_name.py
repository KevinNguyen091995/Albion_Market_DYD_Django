# Generated by Django 4.2.8 on 2023-12-08 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weaponmodel',
            old_name='weapon_name',
            new_name='unique_name',
        ),
    ]
