# Generated by Django 3.1.2 on 2023-03-15 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20230315_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articletag',
            old_name='basic',
            new_name='is_main',
        ),
    ]