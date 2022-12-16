from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),

    path('libros/',views.books),
    path('nuevo_libro/',views.newBook),
    path('libros/obtener_libro/<id>',views.getBook),
    path('editar_libro/',views.editBook),
    path('libros/eliminar_libro/<id>',views.deleteBook),
    


    path('usuarios/',views.users),
    path('nuevo_usuario/',views.newUser),
    path('usuarios/obtener_usuario/<id>',views.getUser),
    path('editar_usuario/',views.editUser),
    path('usuarios/eliminar_usuario/<id>',views.deleteUser),

    path('autores/',views.authors),
    path('nuevo_autor/',views.newAuthor),
    path('autores/obtener_autor/<id>',views.getAuthor),
    path('editar_autor/',views.editAuthor),
    path('autores/eliminar_autor/<id>',views.deleteAuthor),
]
