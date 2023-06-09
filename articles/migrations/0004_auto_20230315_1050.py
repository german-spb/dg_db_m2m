# Generated by Django 3.1.2 on 2023-03-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20230314_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletag',
            options={'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='tag',
            name='tag',
            field=models.ManyToManyField(through='articles.ArticleTag', to='articles.Article'),
        ),
    ]
