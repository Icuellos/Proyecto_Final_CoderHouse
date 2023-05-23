from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
# Create your models here.
class Proyecto(models.Model):
    name = models.CharField(max_length=200)
    # Para retornar los nombres de los proyectos
    def __str__(self):
         return self.name

class Equipos(models.Model):    
    name = models.CharField(max_length=200)

    def __str__(self):
         return self.name
    
class Puntuacion(models.Model):    
     Puntos = models.CharField(max_length=200)
     proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
        
     def __str__(self):
         return self.Puntos
     
class Goleadores(models.Model):    
     Nombre = models.CharField(max_length=200)
     proyecto =models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
     def __str__(self):
         return self.Nombre  
     
class Estadios(models.Model):    
     Nombre = models.CharField(max_length=200)
     proyecto =models.ForeignKey(Proyecto, on_delete=models.CASCADE)  
     
     def __str__(self):
         return self.Nombre      
     
# Eliminar desde aqui en caso de error
class Liga(models.Model):    
     name = models.CharField(max_length=200)
     #proyecto =models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
     def __str__(self):
         return self.name     
    
    
# MODELO PARA CREAR ARTICULO
class Toy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# MODELO PARA CREAR COMETARIOS    
class Comment(models.Model):
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.toy.title}"    