# Generated by Django 5.0 on 2023-12-09 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_api', '0008_offhandmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_name', models.CharField(max_length=50)),
                ('tier', models.IntegerField()),
                ('image_url', models.URLField(default=None)),
                ('item_class', models.CharField(max_length=50)),
                ('item_category', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
