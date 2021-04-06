from personas.models import Persona
from django.shortcuts import render

# Create your views here.
def index(request):
    personas = Persona.objects.all().order_by('-id')
    no_personas = Persona.objects.count()
    return render(request, 'index.html',{
        'no_personas': no_personas,
        'personas': personas
    })
