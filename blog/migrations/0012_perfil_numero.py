# Generated by Django 3.0.6 on 2020-05-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200528_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='numero',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
