# Generated by Django 5.1.1 on 2024-10-08 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_rename_description_post_descricao_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Postagem',
        ),
    ]
