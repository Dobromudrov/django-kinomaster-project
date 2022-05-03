# Generated by Django 4.0.4 on 2022-05-03 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='directors',
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.directors', verbose_name='Режиссёр'),
        ),
    ]
