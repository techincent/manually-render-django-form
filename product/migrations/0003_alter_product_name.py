# Generated by Django 3.2.5 on 2021-07-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_title_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Name max length 250, as helper text', max_length=250),
        ),
    ]
