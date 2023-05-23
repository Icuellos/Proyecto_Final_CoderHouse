
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Equipos, Liga, Toy, Comment
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CrearNuevoFormulario, CrearNuevoProyecto, CrearNuevaLiga, CrearNuevoEquipo, BuscarEquipoForm, BuscarFormulario, ToyForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    title = "Sitio para compartir juguetes que ya no usas!!"
    return render(request, "home.html", 
                  {'title': title})

def about(request):
    username = "icuello"
    return render(request, "About.html", {'username': username})

def Crear_form(request):
   # Proyectos = list(Proyecto.objects.values())
   #Equipos = equipos.objects.all()
   return render(request, 'Crear_form.html',
                 {'form': CrearNuevoFormulario})
   
def Proyectos(request):
   # Proyectos = list(Proyecto.objects.values())
   Ligas = Liga.objects.all()
   return render(request, 'Proyectos.html', {'Ligas': Ligas})   
   
def Crear_Proyecto(request):
    if request.method == 'GET':
     return render(request, 'Crear_Proyecto.html', 
                  {'form': CrearNuevoProyecto()
    })
    else:
        print (request.POST)
        Proyectos = Proyecto.objects.create(name=request.POST["name"])
        return render(request, 'Crear_Proyecto.html', 
                  {'form': CrearNuevoProyecto()
    })
        
def Crear_Liga(request):
    if request.method == 'POST':
        form = CrearNuevaLiga(request.POST)
        if form.is_valid():
            liga = Liga()  
            liga.name = form.cleaned_data['name']  #
            liga.save()  

            return redirect('Proyectos')  
    else:
        form = CrearNuevaLiga()  

    return render(request, 'Crear_Liga.html', {'form': form})

#def Equipo(request):
    #equipos = Equipos.objects.all()
    #return render(request, 'Equipo.html', {'equipos': equipos}) 
def Crear_Equipo(request):
    ligas = Liga.objects.all()

    if request.method == 'POST':
        form = CrearNuevoEquipo(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.liga = form.cleaned_data['liga']
            equipo.save()
            return redirect('Equipo')
    else:
        form = CrearNuevoEquipo()

    return render(request, 'crear_equipo.html', {'form': form, 'ligas': ligas})

#def Crear_Equipo(request):
    if request.method == 'POST':
         form = CrearNuevoEquipo(request.POST)
         if form.is_valid():
            name = form.cleaned_data['name']
            liga = form.cleaned_data['liga']
            equipo = Equipos(name=name, liga=liga)
            #equipo = Equipos(name=name) comentamos esto para ver si podemos guardar equpo en ligas
            equipo.save()
            return redirect('Equipo')   
    else: 
        form = CrearNuevoEquipo()

    return render(request, 'Crear_Equipo.html', {'form': form})

def Equipo(request):
    equipos = Equipos.objects.all()
    return render(request, 'Equipo.html', {'equipos': equipos})    
 

def buscar_equipos(request):
    query = request.GET.get('query')
    equipos = None

    if query is not None:
        equipos = Equipos.objects.filter(name__icontains=query)

    return render(request, 'buscar_equipos.html', {'equipos': equipos, 'query': query})

def detalle_equipo(request, equipo_id):
    equipo = Equipos.objects.get(id=equipo_id)
    return render(request, 'detalle_equipo.html', {'equipo': equipo})  
  
#def detalle_equipo(request, equipo_id):
#    equipo = get_object_or_404(Equipos, id=equipo_id)
#    return render(request, 'detalle_equipo.html', {'equipo': equipo})    

#PARA ELIMINAR EQUIPOS
def eliminar_liga(request, liga_id):
    liga = Liga.objects.get(id=liga_id)
    liga.delete()
    return redirect('Proyectos')

#PARA ELIMINAR UNA LIGA
def eliminar_equipo(request, equipo_id):
    equipo = Equipos.objects.get(id=equipo_id)
    equipo.delete()
    return redirect('Equipo')

#Para crear una vista de los detalles de la liga
def detalle_liga(request, liga_id):
    liga = get_object_or_404(Liga, id=liga_id)
    equipos = liga.equipos.all()
    return render(request, 'detalle_liga.html', {'liga': liga, 'equipos': equipos})

def buscar(request):
    form = BuscarFormulario()

    if request.method == 'POST':
        form = BuscarFormulario(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            tipo_busqueda = form.cleaned_data['tipo_busqueda']

            if tipo_busqueda == 'equipo':
                equipos = Equipos.objects.filter(name__icontains=termino)
                return render(request, 'buscar.html', {'form': form, 'equipos': equipos, 'tipo_busqueda': tipo_busqueda, 'termino': termino})
            elif tipo_busqueda == 'liga':
                ligas = Liga.objects.filter(name__icontains=termino)
                return render(request, 'buscar.html', {'form': form, 'ligas': ligas, 'tipo_busqueda': tipo_busqueda, 'termino': termino})

    return render(request, 'buscar.html', {'form': form})

#FUNCIONES PARA EL PROYECTO fINAL 
def crear_nuevo(request):

   
    
 def home(request):
    toys = Toy.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'toys': toys})

@login_required
def create_toy(request):
    if request.method == 'POST':
        form = ToyForm(request.POST)
        if form.is_valid():
            toy = form.save(commit=False)
            toy.owner = request.user
            toy.save()
            return redirect('home')
    else:
        form = ToyForm()
    return render(request, 'blog/create_toy.html', {'form': form})

@login_required
def delete_toy(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    if toy.owner == request.user:
        toy.delete()
    return redirect('home')

@login_required
def create_comment(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.toy = toy
            comment.user = request.user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'blog/create_comment.html', {'form': form, 'toy': toy})    
    if request.method == 'POST':
        formulario = CrearNuevoFormulario(request.POST)
        if formulario.is_valid():
            # Guardar el formulario y redireccionar
            formulario.save()
            return redirect('index')
    else:
        formulario = CrearNuevoFormulario()
    return render(request, 'crear_nuevo.html', {'formulario': formulario})

