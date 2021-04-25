# Generated by Django 3.2 on 2021-04-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_assets', '0003_auto_20210425_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='digital_key',
            field=models.CharField(max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='note',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='physical_address',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[('available', 'AVAILABLE'), ('in use', 'IN_USE'), ('need maintenance', 'NEED_MAINTENANCE')], default='available', max_length=32),
        ),
    ]
