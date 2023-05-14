# Generated by Django 4.1.7 on 2023-03-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Warehouse_Number', models.PositiveIntegerField()),
                ('Product_Name', models.CharField(max_length=200)),
                ('Product_Quantity', models.PositiveIntegerField()),
                ('Product_State', models.CharField(max_length=200)),
                ('Date_Added', models.DateTimeField()),
            ],
        ),
    ]