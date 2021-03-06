# Generated by Django 3.2.5 on 2021-08-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedDate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Dispatched', 'Dispatched'), ('On The Way', 'On The Way'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
