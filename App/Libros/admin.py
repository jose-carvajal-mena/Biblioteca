from django.contrib import admin
from .models import Autor
from .models import Libro
from .models import Usuario

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Usuario)

