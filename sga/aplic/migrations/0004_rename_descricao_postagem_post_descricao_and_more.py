# Generated by Django 5.1.1 on 2024-10-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_rename_post_postagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postagem',
            old_name='descricao',
            new_name='post_descricao',
        ),
        migrations.RenameField(
            model_name='postagem',
            old_name='titulo',
            new_name='post_titulo',
        ),
        migrations.RemoveField(
            model_name='postagem',
            name='imagem',
        ),
        migrations.AddField(
            model_name='postagem',
            name='post_imagem',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario_email',
            field=models.EmailField(default='usuario@gmail.com', max_length=50),
        ),
    ]
