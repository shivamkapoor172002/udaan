# Generated by Django 5.0.7 on 2024-07-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_record_is_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
