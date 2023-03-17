# Generated by Django 3.1.2 on 2023-03-16 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20230316_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articletag',
            old_name='tag',
            new_name='topic',
        ),
        migrations.AlterField(
            model_name='articletag',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
    ]