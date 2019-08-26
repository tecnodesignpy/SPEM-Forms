from django.shortcuts import render

# Create your views here.
from forms_builder.forms.models import Form


def index(request):
	forms = Form.objects.published()
	return render(request,'index.html',{'forms':forms})




