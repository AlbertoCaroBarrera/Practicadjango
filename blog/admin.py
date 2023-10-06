from django.contrib import admin

# Register your models here.
from .models import Animals,Protectora,Colaborador
admin.site.register(Animals)

admin.site.register(Protectora)

admin.site.register(Colaborador)
