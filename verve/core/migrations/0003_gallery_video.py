# Generated by Django 5.0 on 2023-12-16 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_remove_gallery_title_alter_event_img_alter_event_vid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="gallery",
            name="video",
            field=models.FileField(blank=True, upload_to="gallery/"),
        ),
    ]