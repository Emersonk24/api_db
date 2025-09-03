from django.urls import path
from .views import( 
    personaList,personaByDocumento,Actualizarpersona,EliminarPersona,
    tareaList, tareaByfecha, tareaByrangofecha,tareaBypersona
)

urlpatterns = [
    path('personas/', personaList.as_view(), name='persona-list'),
    path('personas/crear/', personaList.as_view(), name='persona-crear'),
    path('personas/actualizar/<int:pk>/', Actualizarpersona.as_view(), name='persona-actualizar'),
    path('personas/documento/<str:documento>/', personaByDocumento.as_view(), name='persona-by-documento'),
    path('personas/eliminar/<int:pk>/', EliminarPersona.as_view(), name='persona-eliminar'),    
    
     ]

