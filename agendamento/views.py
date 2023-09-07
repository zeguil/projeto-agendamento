# agendamento/views.py
import string, random
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Aluno, Professor, Reserva
from .serializers import AlunoSerializer, ProfessorSerializer, ReservaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def create(self, request, *args, **kwargs):
        # Gerar um código de boleto aleatório com 8 dígitos
        codigo_boleto = ''.join(random.choice(string.digits) for i in range(8))
        
        # Criar a reserva com o código do boleto 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(codigo_boleto=codigo_boleto)
        
        return JsonResponse({'message': 'Reserva criada com sucesso.', 'codigo_boleto': codigo_boleto})
