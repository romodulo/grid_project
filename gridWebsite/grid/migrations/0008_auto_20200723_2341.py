# Generated by Django 3.0.8 on 2020-07-23 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0007_author_blog_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='time',
        ),
        migrations.RemoveField(
            model_name='player',
            name='phone',
        ),
    ]