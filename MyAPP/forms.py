from django import forms
from .models import Liga, Equipos, Proyecto, Toy, Comment

class CrearNuevoFormulario(forms.Form):
    title = forms.CharField(label="Nombre", max_length=200)
    edad = forms.IntegerField(label="Ingrese su edad")
    title2 = forms.CharField(label="Equipo al que pertenece", max_length=200)
    
    
class CrearNuevoProyecto(forms.Form):
    name = forms.CharField(label="Nombre de equipo", max_length=200)
    
# Eliminar desde aqui en caso de error    
class CrearNuevaLiga(forms.Form):
    name = forms.CharField(label="Nombre de la Liga", max_length=200)   
    
#class CrearNuevoEquipo(forms.Form):
#    name = forms.CharField(label="Nombre del Equipo", max_length=200)
#    liga = forms.ModelChoiceField(queryset=Liga.objects.all(), label='Liga')  
class CrearNuevoEquipo(forms.ModelForm):
    name = forms.CharField(label="Nombre del Equipo", max_length=200)
    liga = forms.ModelChoiceField(queryset=Liga.objects.all(), label='Liga')

    class Meta:
        model = Equipos
        fields = ['name', 'liga']
       
class BuscarEquipoForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar equipo', max_length=100)  
    
class BuscarFormulario(forms.Form):
    OPCIONES_BUSQUEDA = [
        ('equipo', 'Equipo'),
        ('liga', 'Liga'),
    ]

    termino = forms.CharField(label='Ingresar dato!!')
    tipo_busqueda = forms.ChoiceField(label='Selecciona Equipo o Liga!!', choices=OPCIONES_BUSQUEDA)
   
#FORMULARIOS PARA PROYECTO FINAL

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ('title', 'description')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
    
    