# Generated by Django 2.2.6 on 2020-05-28 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0003_auto_20200528_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='created',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='created',
        ),
    ]