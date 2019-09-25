from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import JsonResponse
import json
from django.core import serializers

# Create your views here.
from forms_builder.forms.models import Form
import datetime


def index(request):
	forms = Form.objects.published()
	last_expirado = Form.objects.filter(expiry_date__lte=datetime.date.today()).last()
	return render(request,'web/index.html',{'forms':forms,'evento_pasado':last_expirado})



def send_email(request):
    if request.method == "POST":
        print("entro")
        v_nombre 	= request.POST.get('nombre')
        v_email	 	= request.POST.get('email')
        v_asunto 	= request.POST.get('asunto')
        v_mensaje 	= request.POST.get('mensaje')

        html_content = "Nombre: "+v_nombre+" <br>Email: "+v_email+" <br>Mensaje: "+v_mensaje+" <br>Asunto: "+v_asunto
        send_mail("Nuevo Contacto en la Web","","noreply@spem.org.py", ['noreply@spem.org.py'], html_message=html_content)

        data = []
        return JsonResponse(serializers.serialize('json', data), safe= False)
    else:
        print("no entro")
        data = []
        return JsonResponse(serializers.serialize('json', data), safe= False)