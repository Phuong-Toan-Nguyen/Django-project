# Generated by Django 4.2.3 on 2023-08-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_news_items_videourl'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnA_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Date', models.DateField(null=True)),
                ('Detail', models.CharField(max_length=20)),
            ],
        ),
    ]
