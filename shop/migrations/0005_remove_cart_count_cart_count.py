# Generated by Django 4.1.7 on 2023-02-20 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='count',
        ),
        migrations.AddField(
            model_name='cart',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
