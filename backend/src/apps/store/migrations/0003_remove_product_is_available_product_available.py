# Generated by Django 4.1.5 on 2023-01-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20230121_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_available',
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]