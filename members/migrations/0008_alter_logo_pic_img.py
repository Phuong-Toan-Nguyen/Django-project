# Generated by Django 4.2.3 on 2023-08-10 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_logo_pic_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo_pic',
            name='Img',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]