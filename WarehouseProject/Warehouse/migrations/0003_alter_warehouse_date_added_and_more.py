# Generated by Django 4.1.7 on 2023-03-20 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Warehouse', '0002_alter_warehouse_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='Date_Added',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='Product_Quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
