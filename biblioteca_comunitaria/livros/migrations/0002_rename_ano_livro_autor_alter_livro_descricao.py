# Generated by Django 4.1.2 on 2022-10-19 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='ano',
            new_name='autor',
        ),
        migrations.AlterField(
            model_name='livro',
            name='descricao',
            field=models.CharField(max_length=1500),
        ),
    ]
