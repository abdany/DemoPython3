# Generated by Django 3.2.16 on 2022-10-26 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_auto_20221026_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='desc',
            new_name='descr',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='name',
            new_name='namee',
        ),
    ]