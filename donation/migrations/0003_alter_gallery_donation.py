# Generated by Django 4.2.4 on 2024-09-29 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("donation", "0002_donationarea_ngo_gallery_donation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="donation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="donation.donation"
            ),
        ),
    ]
