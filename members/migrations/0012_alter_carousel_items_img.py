# Generated by Django 4.2.3 on 2023-08-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_alter_carousel_items_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel_items',
            name='Img',
            field=models.ImageField(null=True, upload_to='carousels/'),
        ),
    ]
