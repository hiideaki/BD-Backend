# Generated by Django 2.0.6 on 2018-06-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_remove_usuario_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
