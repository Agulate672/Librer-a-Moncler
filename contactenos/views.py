from django.shortcuts import render

def contactenos(request):

    informacion = { 'titulo' : 'Contactenos',
                   'mensaje': 'Gracias por visitar mi pagina, aqui te dejo mis datos por si quieres contactarme!',
                   'email': 'agustinulate04@gmail.com',
                   'telefono':'87069229',
                   'disponibilidad': True
                   }


    return render (request, 'contactenos.html', informacion)
