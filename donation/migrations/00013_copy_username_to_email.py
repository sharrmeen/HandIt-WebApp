from django.db import migrations

def copy_username_to_email(apps, schema_editor):
    User = apps.get_model('auth', 'User')  # Replace 'yourappname' with your app name
    for user in User.objects.all():
        user.email = user.username  # Copy username to email
        user.save()

class Migration(migrations.Migration):
    dependencies = [
        ('donation', '0012_ngo_email'),  # Replace with the last migration name
    ]

    operations = [
        migrations.RunPython(copy_username_to_email),
    ]
