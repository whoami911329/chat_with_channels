# Generated by Django 3.1.5 on 2021-02-14 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_remove_chatroom_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='logo',
        ),
    ]
