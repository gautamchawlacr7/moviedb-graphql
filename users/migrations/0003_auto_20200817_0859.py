# Generated by Django 3.1 on 2020-08-17 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200817_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=50, verbose_name='User Name'),
        ),
    ]