# Generated by Django 5.1.1 on 2024-09-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/'),
        ),
    ]
