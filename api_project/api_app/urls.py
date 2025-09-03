from django.urls import path
from .views import( 
    personaList, personaByDocumento, Actualizarpersona, EliminarPersona,
    tareaList, tareaByfecha, tareaByrangofecha, tareaBypersona,
    EliminarTarea, tareaCrear, ActualizarTarea
)

urlpatterns = [
    # Rutas de personas
    path('personas/', personaList.as_view(), name='persona-list'),
    path('personas/crear/', personaList.as_view(), name='persona-crear'),
    path('personas/actualizar/<int:pk>/', Actualizarpersona.as_view(), name='persona-actualizar'),
    path('personas/documento/<str:documento>/', personaByDocumento.as_view(), name='persona-by-documento'),
    path('personas/eliminar/<int:pk>/', EliminarPersona.as_view(), name='persona-eliminar'),    
    
    # Rutas de tareas
    path('tareas/', tareaList.as_view(), name='tarea-list'),
    path('tareas/crear/', tareaCrear.as_view(), name='tarea-crear'),  # 📌 crear tarea
    path('tareas/actualizar/<int:pk>/', ActualizarTarea.as_view(), name='tarea-actualizar'),  # 📌 actualizar tarea
    path('tareas/fecha/<str:fecha>/', tareaByfecha.as_view(), name='tarea-by-fecha'),
    path('tareas/rango-fecha/<str:fecha_inicio>/<str:fecha_fin>/', tareaByrangofecha.as_view(), name='tarea-by-rango-fecha'),
    path('tareas/persona/<int:persona_id>/', tareaBypersona.as_view(), name='tarea-by-persona'),
    path('tareas/eliminar/<int:pk>/', EliminarTarea.as_view(), name='tarea-eliminar'),
]

