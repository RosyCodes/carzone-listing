# Generated by Django 4.2.4 on 2024-07-13 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='google_plus_link',
            new_name='linkedin_link',
        ),
    ]
