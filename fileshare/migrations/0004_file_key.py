# Generated by Django 4.2.6 on 2023-11-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0003_sharedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='key',
            field=models.BinaryField(default=b'\x00'),
        ),
    ]