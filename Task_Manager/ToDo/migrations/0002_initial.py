# Generated by Django 5.0.1 on 2024-02-01 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ToDo', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.users'),
        ),
    ]