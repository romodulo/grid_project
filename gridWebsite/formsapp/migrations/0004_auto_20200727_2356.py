# Generated by Django 3.0.8 on 2020-07-27 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsapp', '0003_auto_20200727_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='guest5',
            new_name='player2',
        ),
    ]
