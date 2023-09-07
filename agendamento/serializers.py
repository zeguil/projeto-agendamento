# agendamento/serializers.py
from rest_framework import serializers
from .models import Aluno, Professor, Reserva

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    codigo_boleto = serializers.CharField(read_only=True)





