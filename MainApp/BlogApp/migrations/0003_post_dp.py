# Generated by Django 5.1.1 on 2024-10-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_rename_categories_post_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Dp',
            field=models.ImageField(default='media/defaultdp.jpeg', upload_to='media/'),
        ),
    ]
