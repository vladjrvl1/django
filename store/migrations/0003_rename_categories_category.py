# Generated by Django 3.2.3 on 2021-05-22 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_brand_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]
