# Generated by Django 2.2.6 on 2019-12-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopList_app', '0004_auto_20191014_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField()),
                ('item_done', models.BooleanField(default=False)),
            ],
        ),
    ]
