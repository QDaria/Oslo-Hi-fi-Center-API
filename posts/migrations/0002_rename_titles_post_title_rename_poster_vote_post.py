# Generated by Django 4.1.dev20220203190912 on 2022-02-03 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titles',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='poster',
            new_name='post',
        ),
    ]