# Generated by Django 3.1.6 on 2021-02-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recurso'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='posicao',
            field=models.CharField(choices=[('E', 'esquerda'), ('D', 'direita')], default='', max_length=1, verbose_name='Posição Cart'),
        ),
    ]
