from django.db import models    

class personas(models.Model):
    id_peronas = models.AutoField(primary_key=True,editable=False,db_column= 'T001Idpersona')
    nombre = models.CharField(max_length=100,db_column= 'T001Nombre')
    apellido = models.CharField(max_length=100,db_column= 'T001Apellido')
    documento = models.CharField(max_length=20,unique=True,db_column= 'T001Documento')
    email = models.EmailField(unique=True,db_column= 'T001Email')
    activo = models.BooleanField(default=True,db_column= 'T001Activo')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'T001Personas'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
class tareas(models.Model):
    id_tareas = models.AutoField(primary_key=True,editable=False,db_column= 'T002Idtarea')
    titulo = models.CharField(max_length=200,db_column= 'T002Titulo')
    descripcion = models.TextField(db_column= 'T002Descripcion')
    fecha_limite = models.DateField(db_column= 'T002FechaLimite')
    persona = models.ForeignKey(personas, on_delete=models.CASCADE, db_column='T001Idpersona', related_name='tareas')

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'T002Tareas'
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
# Create your models here.
