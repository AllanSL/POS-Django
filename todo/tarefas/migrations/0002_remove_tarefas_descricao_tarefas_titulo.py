# Generated by Django 5.1.7 on 2025-03-20 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefas',
            name='descricao',
        ),
        migrations.AddField(
            model_name='tarefas',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
    ]
