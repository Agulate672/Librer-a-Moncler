from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro

def autores(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        nacionalidad = request.POST.get('nacionalidad')
        descripcion = request.POST.get('descripcion')

        # Crear un nuevo autor con los datos obtenidos
        autor = Autor(
            nombre=nombre,
            apellidos=apellidos,
            nacionalidad=nacionalidad,
            descripcion=descripcion
        )
        autor.save()

    # Obtener todos los autores para pasarlos al template
    autores = Autor.objects.all()

    data = {
        'autores': autores
    }

    return render(request, 'autores.html', data)


def libros(request):
    # Si es una solicitud POST, significa que estamos creando un nuevo libro
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        genero = request.POST.get('genero')
        cantidad_paginas = request.POST.get('cantidad_paginas')
        disponible = request.POST.get('disponible') == 'True'  # Convertir a booleano
        autor_id = request.POST.get('autor')

        # Verificar que los datos requeridos no estén vacíos
        if not titulo or not genero or not cantidad_paginas or not autor_id:
            return render(request, 'libros.html', {'error': 'Por favor, complete todos los campos.'})

        try:
            autor = Autor.objects.get(id=autor_id)
        except Autor.DoesNotExist:
            return render(request, 'libros.html', {'error': 'El autor seleccionado no existe.'})

        # Crear un nuevo libro con los datos obtenidos
        libro = Libro(
            titulo=titulo,
            genero=genero,
            cantidad_paginas=cantidad_paginas,
            disponible=disponible,
            autor=autor
        )
        libro.save()

        # Redirigir al usuario a la misma página para evitar volver a enviar el formulario
        return redirect('libros')

    # Obtener todos los libros para pasarlos al template
    libros = Libro.objects.all()

    # Pasar los datos al template
    data = {
        'libros': libros,
        'autores': Autor.objects.all()  # Para mostrar la lista de autores en el formulario
    }

    # Retornar la respuesta con el listado de libros y el formulario para crear uno nuevo
    return render(request, 'libros.html', data)
        

def crear_autor(request):
    return render(request, 'crear_autor.html')

def editar_autor(request, id):
    # Recupera el autor por ID
    autor = Autor.objects.get(id=id)
    
    # Si se envía el formulario (método POST), actualiza el autor
    if request.method == 'POST':
        autor.nombre = request.POST.get('nombre')
        autor.apellidos = request.POST.get('apellidos')
        autor.nacionalidad = request.POST.get('nacionalidad')
        autor.descripcion = request.POST.get('descripcion')
        autor.save()
        return redirect('autores')  # Redirige a la lista de autores después de guardar
    
    # Pasa el autor al contexto del template
    data = {
        'autor': autor
    }

    return render(request, 'editar_autor.html', data)


def accion_autor (request, id):
    if request.method == 'POST':
        if(request.POST.get('accion') == 'editar'):
            id = request.POST.get('id')
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            nacionalidad = request.POST.get('nacionalidad')
            descripcion = request.POST.get('descripcion')

            autor = Autor.objects.get(id=id)
            autor.nombre = nombre
            autor.apellidos = apellidos
            autor.nacionalidad = nacionalidad
            autor.descripcion = descripcion

            autor.save()

    return redirect('autores')

def eliminar_autor(request, id):
    # Obtén el autor por su ID o muestra un error 404 si no se encuentra
    autor = get_object_or_404(Autor, id=id)
    
    # Elimina el autor de la base de datos
    autor.delete()
    
    # Redirige a la lista de autores después de eliminar
    return redirect('autores')
        
def crear_libro(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        titulo = request.POST.get('titulo')
        genero = request.POST.get('genero')
        cantidad_paginas = request.POST.get('cantidad_paginas')
        disponible = request.POST.get('disponible') == 'True'  # Convertir a booleano
        autor_id = request.POST.get('autor')

        # Verificar que los datos requeridos no estén vacíos
        if not titulo or not genero or not cantidad_paginas or not autor_id:
            return render(request, 'crear_libro.html', {'error': 'Por favor, complete todos los campos.'})

        try:
            autor = Autor.objects.get(id=autor_id)
        except Autor.DoesNotExist:
            return render(request, 'crear_libro.html', {'error': 'El autor seleccionado no existe.'})

        nuevo_libro = Libro(
            titulo=titulo,
            genero=genero,
            cantidad_paginas=cantidad_paginas,
            disponible=disponible,
            autor=autor
        )
        nuevo_libro.save()

        return redirect('libros')  # Redirige a la lista de libros después de guardar

    autores = Autor.objects.all()
    return render(request, 'crear_libro.html', {'autores': autores})

def eliminar_libro(request, id):
    
    libro = get_object_or_404(Libro, id=id)
    
   
    libro.delete()

    return redirect('libros')

def listar_libros(request):
    libros = Libro.objects.all()  # Si tienes un modelo Libro
    return render(request, 'listar_libros.html', {'libros': libros})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)  # Obtener el libro por ID

    if request.method == 'POST':
        # Obtener los datos del formulario
        libro.titulo = request.POST.get('titulo')
        libro.genero = request.POST.get('genero')
        libro.cantidad_paginas = request.POST.get('cantidad_paginas')
        libro.disponible = request.POST.get('disponible') == 'True'  # Convierte el valor en True/False
        libro.autor_id = request.POST.get('autor')  # Establece el autor
        libro.save()
        return redirect('libros')  # Redirige al listado de libros después de guardar

    # Si no es POST, pasa el libro al contexto del template
    data = {
        'libro': libro,
        'autores': Autor.objects.all(),  # También pasas la lista de autores para el select
    }

    return render(request, 'editar_libro.html', data)