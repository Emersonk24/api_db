from django.shortcuts import render
from.models import persona
from .models import tarea
from .serializers import PersonaSerializer, TareaSerializer
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api_project.api_app.models import *
from api_project.api_app.serializers import *
from django.shortcuts import get_object_or_404



class personaList(generics.ListCreateAPIView):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self,request):
        personas =personas.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        if not personas:
            raise NotFound("no se encontraron personas")          
        return Response({ 'success': True,'detail':'listando de personas ' ,'data': serializer.data },status=status.HTTP_200_OK)
        
# crear personas 
class personalista(generics.CreateAPIView):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer

    def post(self,request):
        personas = persona.objects.all()
        serializer = PersonaSerializer(data=request.data)
        def post(self,request):
            serializer = PersonaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({ 'success': True,'detail':'persona creada' ,'data': serializer.data },status=status.HTTP_201_CREATED)
        
# actuliizar personas

class Actualizarpersona(generics.UpdateAPIView):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer

    def put(self,request,pk):
            personas = get_object_or_404(persona, pk=pk)
            email = request.data.get('email',None)
           
            if email and personas.email != email:
                if persona.objects.filter(email=email).extists(pk=pk).extists():
                    return Response({'email':['persona with this email already exists .'] },status=status.HTTP_400_BAD_REQUEST)


            serializer = PersonaSerializer(personas, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({ 'success': True,'detail':'persona actualizada' ,'data': serializer.data },status=status.HTTP_200_OK)

# buscar personas por documento

class personaByDocumento(generics.RetrieveAPIView):
    serializer_class = PersonaSerializer

    def get(self, request, documento):
        personas = persona.objects.filter(documento=documento).first()
        if not personas:
            return Response({'detail':'no se encontro persona con ese documeto. '})
        serializer = PersonaSerializer(personas)
        return Response({ 'success': True,'detail':'persona encontrada' ,'data': serializer.data },status=status.HTTP_200_OK)
    
# eliminar personas 

class EliminarPersona(generics.DestroyAPIView):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer

    def delete(self, request, pk):
        personas = get_object_or_404(persona, pk=pk)
        personas.delete()
        return Response(
            {'success': True, 'detail': 'Persona eliminada correctamente'},
            status=status.HTTP_204_NO_CONTENT
        )

#  Listar tareas
class tareaList(generics.ListCreateAPIView):
    queryset = tarea.objects.all()
    serializer_class = TareaSerializer

    def get(self, request):
        tareas = tarea.objects.all()
        serializer = TareaSerializer(tareas, many=True)
        if not tareas:
            raise NotFound("No se encontraron tareas")
        return Response({'success': True, 'detail': 'Listando tareas', 'data': serializer.data}, status=status.HTTP_200_OK)


#  Crear tareas
class tareaCrear(generics.CreateAPIView):
    queryset = tarea.objects.all()
    serializer_class = TareaSerializer

    def post(self, request):
        serializer = TareaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Tarea creada', 'data': serializer.data}, status=status.HTTP_201_CREATED)


#  Actualizar tareas
class ActualizarTarea(generics.UpdateAPIView):
    queryset = tarea.objects.all()
    serializer_class = TareaSerializer

    def put(self, request, pk):
        tareas = get_object_or_404(tarea, pk=pk)
        serializer = TareaSerializer(tareas, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Tarea actualizada', 'data': serializer.data}, status=status.HTTP_200_OK)


#  Eliminar tareas
class EliminarTarea(generics.DestroyAPIView):
    queryset = tarea.objects.all()
    serializer_class = TareaSerializer

    def delete(self, request, pk):
        tareas = get_object_or_404(tarea, pk=pk)
        tareas.delete()
        return Response({'success': True, 'detail': 'Tarea eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)


#  Buscar tareas por fecha
class tareaByfecha(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, fecha):
        tareas = tarea.objects.filter(fecha_limite=fecha)
        if not tareas:
            return Response({'detail': 'No se encontraron tareas con esa fecha.'})
        serializer = TareaSerializer(tareas, many=True)
        return Response({'success': True, 'detail': 'Tareas encontradas', 'data': serializer.data}, status=status.HTTP_200_OK)


# Buscar tareas por rango de fechas
class tareaByrangofecha(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, fecha_inicio, fecha_fin):
        tareas = tarea.objects.filter(fecha_limite__range=[fecha_inicio, fecha_fin])
        if not tareas:
            return Response({'detail': 'No se encontraron tareas en ese rango de fechas.'})
        serializer = TareaSerializer(tareas, many=True)
        return Response({'success': True, 'detail': 'Tareas encontradas', 'data': serializer.data}, status=status.HTTP_200_OK)


# Buscar tareas por persona
class tareaBypersona(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, persona_id):
        tareas = tarea.objects.filter(persona__id_personas=persona_id)
        if not tareas:
            return Response({'detail': 'No se encontraron tareas para esa persona.'})
        serializer = TareaSerializer(tareas, many=True)
        return Response({'success': True, 'detail': 'Tareas encontradas', 'data': serializer.data}, status=status.HTTP_200_OK)