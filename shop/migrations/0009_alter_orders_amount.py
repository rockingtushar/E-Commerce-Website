# Generated by Django 5.0.4 on 2024-08-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
