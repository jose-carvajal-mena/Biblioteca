from django.shortcuts import render,redirect
from .models import Autor
from .models import Libro
from .models import Usuario
from django.contrib import messages


def home(request):
    return render(request, "index.html")

def books(request):
    return render(request, "libros.html")

def authors(request):
    return render(request, "autores.html")


# Inicio vistas de usuarios
def users(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarios.html", {"usuarios":usuarios})

def newUser(request):
    email = request.POST["txtEmail"]
    rol = request.POST["txtRol"]
    password = request.POST["txtPassword"]

    Usuario.objects.create(email=email, rol=rol, password=password)
    messages.success(request, "Usuario Agregado con exito")
    return redirect("/")

def getUser(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request,"editarUsuario.html",{"usuario":usuario})

def editUser(request):
    id = request.POST["txtId"]
    email = request.POST["txtEmail"]
    rol = request.POST["txtRol"]
    password = request.POST["txtPassword"]

    usuario = Usuario.objects.get(id=id)
    usuario.email = email
    usuario.rol = rol
    usuario.password = password
    usuario.save()
    messages.success(request, "Usuario editado con exito")
    return redirect("/")

def deleteUser(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    messages.success(request, "Usuario eliminado con exito")
    return redirect("/")
# Fin vistas de usuarios


# Inicio vistas de autores
def authors(request):
    autores = Autor.objects.all()
    return render(request, "autores.html", {"autores":autores})

def newAuthor(request):
    nombre = request.POST["txtNombre"]
    sexo = request.POST["txtSexo"]
    fecha_nacimiento = request.POST["txtNacimiento"]
    nacionalidad = request.POST["txtNacionalidad"]
    apellido = request.POST["txtApellido"]
   
    messages.success(request, "Autor Agregado con exito")
    Autor.objects.create(nombre=nombre, sexo=sexo, fecha_nacimiento=fecha_nacimiento, nacionalidad=nacionalidad, apellido=apellido)
 
    return redirect("/")

def getAuthor(request, id):
    autor = Autor.objects.get(id=id)
    return render(request,"editarAutor.html",{"autor":autor})

def editAuthor(request):
    id = request.POST["txtId"]
    nombre = request.POST["txtNombre"]
    sexo = request.POST["txtSexo"]
    fecha_nacimiento = request.POST["txtNacimiento"]
    nacionalidad = request.POST["txtNacionalidad"]
    apellido = request.POST["txtApellido"]

    autor = Autor.objects.get(id=id)
    autor.nombre = nombre
    autor.sexo = sexo
    autor.fecha_nacimiento = fecha_nacimiento
    autor.nacionalidad = nacionalidad
    autor.apellido = apellido
    autor.save()
    messages.success(request, "Autor actualizado con exito")
    return redirect("/")

def deleteAuthor(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    messages.success(request, "Autor eliminado con exito")
    return redirect("/")
# Fin vistas de autores


# Inicio vistas de libros
def books(request):
    libros = Libro.objects.all()
    return render(request, "libros.html", {"libros":libros})

def newBook(request):
    isbn = request.POST["txtIsbn"]
    titulo = request.POST["txtTitulo"]
    numero_paginas = request.POST["txtPaginas"]
    descripcion = request.POST["txtDescripcion"]
    portada = request.POST["txtPortada"]
    
    Libro.objects.create(isbn=isbn, titulo=titulo, numero_paginas=numero_paginas, descripcion=descripcion, portada=portada)

    messages.success(request, "Libro Agregado con exito")
    
    return redirect("/")

def getBook(request, id):
    libro = Libro.objects.get(id=id)
    return render(request,"editarLibro.html",{"libro":libro})

def editBook(request):
    id = request.POST["txtId"]
    isbn = request.POST["txtIsbn"]
    titulo = request.POST["txtTitulo"]
    numero_paginas = request.POST["txtPaginas"]
    descripcion = request.POST["txtDescripcion"]
    portada = request.POST["txtPortada"]

    libro = Libro.objects.get(id=id)
    libro.isbn = isbn
    libro.titulo = titulo
    libro.numero_paginas = numero_paginas
    libro.descripcion = descripcion
    libro.portada = portada
    libro.save()
    messages.success(request, "Libro actualizado con exito")
    return redirect("/")

def deleteBook(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    messages.success(request, "Libro eliminado con exito")
    return redirect("/")
# Fin vistas de libros


