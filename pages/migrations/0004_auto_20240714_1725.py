# Generated by Django 3.0.7 on 2024-07-14 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_google_plus_link_team_linkedin_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
