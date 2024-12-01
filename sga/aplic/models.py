import os
from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=180)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def save(self, *args, **kwargs):
        if self.image:
            nome_imagem, extensao = os.path.splitext(self.image.name)
            self.image.name = f'{self.title.replace(" ", "_")}{extensao}'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
