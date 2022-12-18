from django.db import models
from django.contrib.auth.models import *
from django.utils import timezone

# Create your models here.
class Usuarios(models.Model):
    username = models.CharField(max_length=20, default="Anonymus User")
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    fecnac=models.DateField()
    telefono=models.IntegerField()
    email=models.EmailField()
    
    
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)        
    
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    
    class Meta:
        ordering = ['timestamp']
        
    def __str__(self):
        return f'{self.user.username}: {self.content}'