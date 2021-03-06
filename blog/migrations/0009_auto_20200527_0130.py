# Generated by Django 3.0.6 on 2020-05-27 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200525_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitrine',
            name='descricao',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('categoria', models.CharField(choices=[('Informatica', 'Informática'), ('Celulares', 'Celulares'), ('Moda', 'Moda')], max_length=20)),
                ('descricao', models.TextField(default='', null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantidade', models.PositiveSmallIntegerField(default=0)),
                ('data_criacao', models.DateField()),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Vitrine')),
            ],
        ),
    ]
