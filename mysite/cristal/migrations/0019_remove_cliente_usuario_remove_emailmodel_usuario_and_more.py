# Generated by Django 4.2.1 on 2023-05-12 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cristal', '0018_cliente_usuario_emailmodel_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='emailmodel',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='tarefamodel',
            name='usuario',
        ),
    ]