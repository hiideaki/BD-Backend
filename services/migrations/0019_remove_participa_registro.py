# Generated by Django 2.0.6 on 2018-06-18 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_remove_comparece_grupo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participa',
            name='registro',
        ),
    ]
