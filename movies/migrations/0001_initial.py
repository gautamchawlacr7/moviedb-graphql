# Generated by Django 3.1 on 2020-08-16 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Movie Id')),
                ('name', models.CharField(max_length=100, verbose_name='Movie Name')),
                ('avg_rating', models.FloatField(verbose_name='Average Rating')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=50, unique=True, verbose_name='Code Name')),
                ('movie_list', models.ManyToManyField(to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.user')),
            ],
        ),
    ]
