from django.contrib import admin
from .models import *

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )	
def _register(model, admin_class):
    admin.site.register(model, admin_class)
	
	
_register(Evento,EventoAdmin)