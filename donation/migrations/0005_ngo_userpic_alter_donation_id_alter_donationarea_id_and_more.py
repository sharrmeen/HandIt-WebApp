# Generated by Django 4.2.16 on 2024-10-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donation", "0004_auto_20241003_2119"),
    ]

    operations = [
        migrations.AddField(
            model_name="ngo",
            name="userpic",
            field=models.FileField(null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="donation",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="donationarea",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="donor",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="ngo",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
