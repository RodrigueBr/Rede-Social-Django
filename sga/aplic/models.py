from django.db import models
import os

# Create your models here.

class Postagem(models.Model):
    post_titulo = models.CharField(primary_key=True, max_length=100)
    post_descricao = models.TextField(max_length=180)
    post_imagem = models.ImageField(upload_to='images/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.post_imagem:
            nome_imagem, extensao = os.path.splitext(self.post_imagem.name)
            self.post_imagem.name = f'{self.post_titulo.replace(" ", "_")}{extensao}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.post_titulo

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

class Usuario(models.Model):
    usuario_username = models.CharField(primary_key=True, max_length=15, default='')
    usuario_nome = models.CharField(max_length=20, default='')
    usuario_sobrenome = models.EmailField(max_length=20, default='')
    usuario_senha = models.CharField(max_length=30, default='')
    usuario_idade = models.IntegerField(default=0)

    def __str__(self):
        return self.usuario_username

    class Meta:
        verbose_name = 'Cadastro de Usuário'
        verbose_name_plural = 'Cadastro de Usuários'

class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario_conteudo = models.TextField()
    comentario_data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} em {self.postagem}'

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

class Report(models.Model):
    usuario_reportado = models.ForeignKey(Usuario, related_name='Reports', on_delete=models.CASCADE)
    Report_motivo = models.TextField(max_length=100, default='')
    Report_criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report de {self.usuario_reportado}'

class Perfil(models.Model):
    perfil_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    perfil_biografia = models.TextField(max_length=150, default='')
    perfil_interesses = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'Pefil de {self.perfil_usuario}'

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
