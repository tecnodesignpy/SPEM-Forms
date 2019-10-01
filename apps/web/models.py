from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext, ugettext_lazy as _

# Create your models here.


class Evento(models.Model):
	nombre_evento 		= models.CharField(max_length=200, blank=False, null=False)
	habilitado			= models.BooleanField(default=False)
	portada 			= models.ImageField(default='', blank=True, null=True, upload_to='portadas')
	descripcion_corta 	= RichTextField(blank=True)
	inicio_evento 		= models.DateField(_("Inicio del Evento"),
	    help_text=_("Para la cuenta regresiva"),
	    blank=True, null=True)

	def __str__(self):
	    return str(self.nombre_evento)