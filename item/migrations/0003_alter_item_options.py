# Generated by Django 4.2.5 on 2023-09-13 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-created', 'category', 'name')},
        ),
    ]
