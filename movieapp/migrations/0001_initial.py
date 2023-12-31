# Generated by Django 4.2.5 on 2023-09-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('poster', models.URLField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('year_release', models.IntegerField()),
                ('metacritic_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('runtime', models.IntegerField()),
                ('genres', models.ManyToManyField(to='movieapp.genre')),
            ],
        ),
    ]
