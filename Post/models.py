from django.db import models

# Create your models here.
class Reserva(models.Model):

    nombre = models.CharField(max_length=40)
    appelido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()

class Pedido(models.Model):

    comida = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    hora_de_entrega = models.TimeField()

class Evento(models.Model):

    tipo_servicio = models.CharField(max_length=40) 
    direccion = models.CharField(max_length=40)
    cantidad_personas = models.IntegerField()
    fecha_de_evento = models.DateField()

class Contacto(models.Model):

    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    asunto = models.CharField(max_length=40)
    mensaje = models.CharField(max_length=400)