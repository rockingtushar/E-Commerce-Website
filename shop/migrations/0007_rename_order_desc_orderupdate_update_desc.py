# Generated by Django 5.0.4 on 2024-08-25 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate_alter_orders_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderupdate',
            old_name='Order_desc',
            new_name='update_desc',
        ),
    ]
