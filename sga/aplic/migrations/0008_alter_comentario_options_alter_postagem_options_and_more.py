# Generated by Django 5.1.1 on 2024-10-08 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0007_alter_postagem_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name': 'Comentário', 'verbose_name_plural': 'Comentários'},
        ),
        migrations.AlterModelOptions(
            name='postagem',
            options={'verbose_name': 'Postagem', 'verbose_name_plural': 'Postagens'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Cadastro_Usuário', 'verbose_name_plural': 'Cadastro_Usuários'},
        ),
    ]