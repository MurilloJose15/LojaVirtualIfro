# Generated by Django 4.2.4 on 2023-08-16 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='teste',
        ),
    ]