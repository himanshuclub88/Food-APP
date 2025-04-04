# Generated by Django 5.0.4 on 2024-04-22 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Item_desc',
            new_name='item_desc',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Item_name',
            new_name='item_name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Item_price',
            new_name='item_price',
        ),
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.shutterstock.com/image-vector/coming-soon-page-interface-design-260nw-1324789343.jpg', max_length=500),
        ),
    ]
