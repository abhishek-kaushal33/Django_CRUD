# Generated by Django 4.1.1 on 2022-10-29 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0004_rename_rpassword_user_reenter_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='reenter_password',
            new_name='rpassword',
        ),
    ]
