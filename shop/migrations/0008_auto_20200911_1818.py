# Generated by Django 3.1 on 2020-09-11 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]