from django.contrib import admin
from .models import Postagem, Usuario, Comentario, Report, Perfil
# Register your models here.

admin.site.register(Postagem)
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Report)
admin.site.register(Perfil)