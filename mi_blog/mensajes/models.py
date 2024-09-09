# mensajes/models.py
from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name='remitente', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='destinatario', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.remitente} a {self.destinatario}"
