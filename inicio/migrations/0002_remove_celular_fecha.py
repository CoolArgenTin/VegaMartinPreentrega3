# Generated by Django 5.1.2 on 2024-11-02 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celular',
            name='fecha',
        ),
    ]
