# Generated by Django 4.0.4 on 2022-05-02 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='tilte',
            new_name='title',
        ),
    ]