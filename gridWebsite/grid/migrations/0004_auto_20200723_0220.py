# Generated by Django 3.0.8 on 2020-07-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0003_auto_20200723_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
