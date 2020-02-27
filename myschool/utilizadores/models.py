from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Perfil(models.Model):
    """
    Objeto Perfil, responsável por armazenar informação relativa ao perfil
    de cada utilizador da aplicação.
    Quando um utilizador se regista na aplicação, um perfil é criado
    automaticamente.
    """
    utilizador = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(
        default='default.jpg', upload_to='img_perfil')

    def __str__(self):
        return f'Perfil de {self.utilizador.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.imagem.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.imagem.path)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
