# Generated by Django 4.2.1 on 2023-06-02 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_address_city_alter_address_state_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lname',
        ),
    ]
