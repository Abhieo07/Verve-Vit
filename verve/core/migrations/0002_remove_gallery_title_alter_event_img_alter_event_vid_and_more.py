# Generated by Django 5.0 on 2023-12-16 21:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gallery",
            name="title",
        ),
        migrations.AlterField(
            model_name="event",
            name="img",
            field=models.ImageField(blank=True, default="default.png", upload_to=""),
        ),
        migrations.AlterField(
            model_name="event",
            name="vid",
            field=models.FileField(blank=True, default="default.mp4", upload_to=""),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="image",
            field=models.ImageField(upload_to="gallery/"),
        ),
        migrations.AlterField(
            model_name="highlight",
            name="image",
            field=models.ImageField(blank=True, upload_to="highlights/"),
        ),
        migrations.AlterField(
            model_name="highlight",
            name="video",
            field=models.FileField(blank=True, upload_to="highlights/"),
        ),
    ]
