# Generated by Django 5.0.5 on 2024-05-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_project_members'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='members', to='user.user'),
        ),
    ]
