# Generated by Django 2.2.6 on 2019-12-15 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShopList_app', '0005_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='ShopList_app.List'),
        ),
    ]
