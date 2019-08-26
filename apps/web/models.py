from django.db import models

# Create your models here.


class Evento(models.Model):
	nombre_evento 	= models.CharField(max_length=200, blank=False, null=False)
	habilitado		= models.BooleanField(default=False)
