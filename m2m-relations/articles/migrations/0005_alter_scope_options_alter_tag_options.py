# Generated by Django 4.1.7 on 2023-02-17 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_rename_title_tag_name_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Редактирование статьи', 'verbose_name_plural': 'Редактирование статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Создать раздел', 'verbose_name_plural': 'Создать раздел'},
        ),
    ]
