# Generated by Django 2.2.5 on 2022-03-07 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220307_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='langauge',
            new_name='language',
        ),
    ]