# Generated by Django 3.1.4 on 2024-10-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_alter_gallery_donation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='User',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='donation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='donationarea',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
