# Generated by Django 4.2.8 on 2023-12-08 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market_api', '0004_alter_weaponmodel_unique_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='weaponmodel',
            name='item_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weaponmodel', to='market_api.itemdescriptionmodel'),
        ),
    ]
