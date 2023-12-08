# Generated by Django 4.2.8 on 2023-12-08 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market_api', '0002_rename_weapon_name_weaponmodel_unique_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weaponmodel',
            name='unique_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market_api.itemdescriptionmodel', to_field='unique_name'),
        ),
    ]
