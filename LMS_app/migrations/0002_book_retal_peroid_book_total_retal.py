# Generated by Django 4.1.7 on 2023-02-17 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='retal_peroid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='total_retal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
