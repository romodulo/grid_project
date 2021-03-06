# Generated by Django 3.0.8 on 2020-07-27 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formsapp', '0005_auto_20200728_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courttime',
            name='court',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formsapp.Court'),
        ),
        migrations.AlterField(
            model_name='courttime',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formsapp.Time'),
        ),
    ]
