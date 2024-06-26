# Generated by Django 5.0.5 on 2024-05-07 14:37

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('phone', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('date_joined', models.DateField(default=datetime.date.today)),
                ('friends', models.ManyToManyField(to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='user.user')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='user.user')),
            ],
        ),
    ]
