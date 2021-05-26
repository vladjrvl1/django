# Generated by Django 3.2.3 on 2021-05-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210525_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name': 'Device', 'verbose_name_plural': 'Devices'},
        ),
        migrations.AlterField(
            model_name='device',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='products/%y/%m/%d/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='device',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='products/%y/%m/%d/', verbose_name='Photo 1'),
        ),
        migrations.AlterField(
            model_name='device',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='products/%y/%m/%d/', verbose_name='Photo 2'),
        ),
        migrations.AlterField(
            model_name='device',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='products/%y/%m/%d/', verbose_name='Photo 3'),
        ),
        migrations.AlterField(
            model_name='device',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='products/%y/%m/%d/', verbose_name='Photo 4'),
        ),
    ]