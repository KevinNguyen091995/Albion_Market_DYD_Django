# Generated by Django 4.2.8 on 2023-12-08 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market_api', '0006_remove_weaponmodel_item_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemdescriptionmodel',
            old_name='description',
            new_name='item_name',
        ),
    ]
