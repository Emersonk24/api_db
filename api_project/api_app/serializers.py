from rest_framework import serializers
from .models import personas, tareas

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = personas
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tareas
        fields = '__all__'
        