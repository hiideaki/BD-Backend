# Generated by Django 2.0.6 on 2018-06-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_auto_20180618_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
