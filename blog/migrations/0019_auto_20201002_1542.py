# Generated by Django 3.0.6 on 2020-10-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200925_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, default='user.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='produto',
            name='foto',
            field=models.ImageField(blank=True, default='produto.jpeg', upload_to=''),
        ),
        migrations.AddField(
            model_name='vitrine',
            name='foto',
            field=models.ImageField(blank=True, default='vitrine.png', upload_to=''),
        ),
    ]
