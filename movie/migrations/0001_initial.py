# Generated by Django 4.2.6 on 2024-01-19 18:51

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(editable=False, populate_from="name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(editable=False, populate_from="name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Movies",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=300)),
                ("image", models.FileField(upload_to="movie_pic")),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(editable=False, populate_from="name"),
                ),
                ("video", models.FileField(upload_to="movie_video")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movie.category"
                    ),
                ),
                ("genre", models.ManyToManyField(to="movie.genre")),
            ],
        ),
    ]
