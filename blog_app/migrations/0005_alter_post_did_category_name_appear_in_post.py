# Generated by Django 5.0.1 on 2024-02-12 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_post_did_category_name_appear_in_post_post_num_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='did_category_name_appear_in_post',
            field=models.BooleanField(default=False),
        ),
    ]
