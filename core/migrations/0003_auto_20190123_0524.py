# Generated by Django 2.0.6 on 2019-01-23 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190123_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
