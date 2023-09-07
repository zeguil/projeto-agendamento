from django.contrib import admin
from .models import Aluno, Professor, Reserva

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Reserva)
