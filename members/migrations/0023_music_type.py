# Generated by Django 4.2.3 on 2023-08-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0022_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='Type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]