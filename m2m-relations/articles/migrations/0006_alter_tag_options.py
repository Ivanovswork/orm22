# Generated by Django 4.1.7 on 2023-02-17 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_scope_options_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Создать раздел', 'verbose_name_plural': 'раздел'},
        ),
    ]
