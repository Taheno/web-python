# Generated by Django 5.1.4 on 2024-12-07 14:56

import phone_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_agenda_alter_task_options_alter_task_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='telefone',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]
