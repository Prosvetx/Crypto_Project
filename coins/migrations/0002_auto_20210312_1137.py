# Generated by Django 3.1.7 on 2021-03-12 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coin',
            old_name='synbol',
            new_name='symbol',
        ),
    ]
