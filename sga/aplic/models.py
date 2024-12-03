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

class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class ProfileReport(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_profiles')
    reason = models.TextField(verbose_name="Motivo do Report", default="Motivo não especificado")
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reported_by} reportou {self.reported_user} em {self.report_date}"