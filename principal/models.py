# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
def some_function():
    from .models import Beneficiarios, Proyectos,Documentos

class Proyectos(models.Model):
    proyecto_id = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=100, blank=True, null=True)
    actividad = models.ForeignKey('Actividades', null=True, blank=True, on_delete=models.CASCADE)
    beneficiario = models.ForeignKey('Beneficiarios', null=True, blank=True, on_delete=models.SET_NULL)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True, choices=[
        ('Activo', 'Activo'),
        ('Completado', 'Completado'),
        ('Pendiente', 'Pendiente'),
        ('Cancelado', 'Cancelado'),
    ])
    def __str__(self):
        return self.nombre_proyecto
    
    class Meta:
        db_table = 'proyectos'

class Beneficiarios(models.Model):
    beneficiario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=4, blank=True, null=True, choices=[
        ('M','M'),
        ('F','F'),
        ('Otro','Otro'),
    ] )

    telefono = models.CharField(max_length=20, blank=True, null=True)
    grupo_etnico = models.CharField(max_length=14, blank=True, null=True, choices=[
        ('Campesino','Campesino'),
        ('Indígena','Indígena'),
        ('Mestizo','Mestizo'),
        ('Afrocolombiano','Afrocolombiano'),
        ('Palenquero','Palenquero'),
        ('Raizal','Raizal'),
        ('Rom','Rom'),
        ('Otra','Otra'),
        ('Ninguna','Ninguna'),
    ])
    email = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateTimeField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    class Meta:
        db_table = 'beneficiarios'

class Actividades(models.Model):
    actividad_id = models.AutoField(primary_key=True)
    nombre_actividad = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_actividad = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[
        ('Completada', 'Completada'),
        ('Pendiente', 'Pendiente'),
        ('Cancelada', 'Cancelada')
    ], blank=True, null=True)

    def __str__(self):
        return self.nombre_actividad
    class Meta:
        db_table = 'actividades'
        db_table_comment = 'Actividades de cada proyecto'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class BeneficiariosProyectos(models.Model):
    beneficiario_proyecto_id = models.AutoField(primary_key=True)
    beneficiario = models.ForeignKey('Beneficiarios', null=True, blank=True, on_delete=models.SET_NULL)
    proyecto = models.ForeignKey('Proyectos', on_delete=models.CASCADE, db_column='proyecto_id')

    class Meta:
        managed = False
        db_table = 'beneficiarios_proyectos'
        db_table_comment = 'Esta tabla establece una relacion entres Beneficiarios y Proyectos en la fundacion'

class BeneficiariosRegiones(models.Model):
    beneficiario_region_id = models.AutoField(primary_key=True)
    beneficiario_id = models.IntegerField()
    region_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'beneficiarios_regiones'
        db_table_comment = 'Esta tabla establece una relacion entre beneficiarios y regiones'

class CategoriasProyectos(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias_proyectos'
        db_table_comment = 'Esta tabla establece una relacion entre la tabla de categorias y proyectos'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fundacion.django_session'

class Documentos(models.Model):
    documento_id = models.AutoField(primary_key=True)
    beneficiario = models.ForeignKey('Beneficiarios', null=True, blank=True, on_delete=models.SET_NULL)
    TIPO_DOCUMENTO_CHOICES = [
        ('Cédula', 'Cédula'),
        ('Tarjeta de identidad', 'Tarjeta de identidad'),
        ('Cédula de extranjería', 'Cédula de extranjería'),
        ('Pasaporte', 'Pasaporte')
    ]
    tipo_documento = models.CharField(max_length=100, choices=TIPO_DOCUMENTO_CHOICES, blank=False, null=False)
    numero_documento = models.CharField(max_length=50, blank=False, null=False)
    nombre_documento = models.CharField(max_length=255, blank=True, null=True)
    ruta_documento = models.CharField(max_length=255, blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'documentos'
        db_table_comment = 'Esta tabla se encarga de guardar los documentos que tiene cada beneficiario en la fundación'

class Donaciones(models.Model):
    donacion_id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey('Proyectos', on_delete=models.CASCADE, db_column='proyecto_id')
    beneficiario = models.ForeignKey('Beneficiarios', null=True, blank=True, on_delete=models.SET_NULL)
    donante = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_donacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'donaciones'
        db_table_comment = 'Esta tabla se encarga de guardar las donaciones que se le realizan a la fundacion'

class Notificaciones(models.Model):
    notificacion_id = models.AutoField(primary_key=True)
    beneficiario = models.ForeignKey('Beneficiarios', null=True, blank=True, on_delete=models.SET_NULL)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notificaciones'
        db_table_comment = 'Esta tabla se encarga de guardar las notificaciones que se le realizan a cada usuario en la fundacion'

class Permisos(models.Model):
    permiso_id = models.AutoField(primary_key=True)
    nombre_permiso = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permisos'
        db_table_comment = 'Esta tabla se encarga de guardar los permisos que se le asignan a cada rol'      
class ProyectosRegiones(models.Model):
    proyecto_region_id = models.AutoField(primary_key=True)
    proyecto_id = models.IntegerField()
    region_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proyectos_regiones'
        db_table_comment = 'Esta tabla establece una relacion entre proyectos y regiones '

class Recursos(models.Model):
    recurso_id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey('Proyectos', on_delete=models.CASCADE, db_column='proyecto_id')
    tipo_recurso = models.CharField(max_length=100,choices=[
    ('Economicos','Economicos'),
    ('Materiales','Materiales'),
    ('Tecnologicos','Tecnologicos'),
    ])
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recursos'
        db_table_comment = 'Esta tabla se encarga de guardar los recursos que tiene la fundacion'

class Regiones(models.Model):
    region_id = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=5,choices=[
    ('Cauca','Cauca'),
    ])
    municipio = models.CharField(max_length=22,choices=[
    ('Almaguer','Almaguer'),
    ('Argelia','Argelia'),
    ('Bolívar','Bolívar'),
    ('Buenos Aires','Buenos Aires'),
    ('Cajibío','Cajibío'),
    ('Caldono','Caldono'),
    ('Caloto','Caloto'),
    ('Corinto','Corinto'),
    ('El Tambo','El Tambo'),
    ('Florencia','Florencia'),
    ('Guachené','Guachené'),
    ('Guapí','Guapí'),
    ('Inzá','Inzá'),
    ('Jambaló','Jambaló'),
    ('La Sierra','La Sierra'),
    ('La Vega','La Vega'),
    ('López de Micay','López de Micay'),
    ('Mercaderes','Mercaderes'),
    ('Miranda','Miranda'),
    ('Morales','Morales'),
    ('Padilla','Padilla'),
    ('Páez','Páez'),
    ('Patía','Patía'),
    ('Piamonte','Piamonte'),
    ('Piendamó','Piendamó'),
    ('Popayán','Popayán'),
    ('Puerto Tejada','Puerto Tejada'),
    ('Puracé','Puracé'),
    ('Rosas','Rosas'),
    ('San Sebastián','San Sebastián'),
    ('Santa Rosa','Santa Rosa'),
    ('Santander de Quilichao','Santander de Quilichao'),
    ('Silvia','Silvia'),
    ('Sotará','Sotará'),
    ('Suárez','Suárez'),
    ('Timbío','Timbío'),
    ('Timbiquí','Timbiquí'),
    ('Toribío','Toribío'),
    ('Totoró','Totoró'),
    ('Villa Rica','Villa Rica')
    ])
    vereda = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.municipio}-{self.vereda}"

    class Meta:
        managed = False
        db_table = 'regiones'
        db_table_comment = 'Regiones donde están ubicados los beneficiarios, incluyendo departamento, municipio y vereda'

class Roles(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'
        db_table_comment = 'Esta tabla se encarga de guardar los roles que tiene cada ususario en la fundacion'

class RolesPermisos(models.Model):
    rol_permiso_id = models.AutoField(primary_key=True)
    rol_id = models.IntegerField()
    permiso_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'roles_permisos'
        db_table_comment = 'Esta tabla establece una relacion entre roles y permisos'

class Seguimientos(models.Model):
    seguimiento_id = models.AutoField(primary_key=True)
    beneficiario = models.ForeignKey('Beneficiarios', null=True, blank=True, on_delete=models.SET_NULL)
    proyecto = models.ForeignKey('Proyectos', on_delete=models.CASCADE, db_column='proyecto_id')
    region = models.ForeignKey('Regiones', null=True, blank=True, on_delete=models.SET_NULL)
    fecha_seguimiento = models.DateField()
    tipo_seguimiento = models.CharField(max_length=100)
    detalle = models.TextField(blank=True, null=True)
    responsable = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'seguimientos'
        db_table_comment = 'Esta tabla se encarga de guardar todos los seguimientos que se le realizan a los proyectos'

class SesionesFormacion(models.Model):
    sesion_id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey('Proyectos', on_delete=models.CASCADE, db_column='proyecto_id')
    beneficiario = models.ForeignKey('Beneficiarios', null=True, blank=True, on_delete=models.SET_NULL)
    region = models.ForeignKey('Regiones', null=True, blank=True, on_delete=models.SET_NULL)
    tema = models.CharField(max_length=255)
    fecha_sesion = models.DateField()
    duracion = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'sesiones_formacion'
        db_table_comment = 'Esta tabla guarda todas las sesiones de formación que se hacen acerca de los proyectos'

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    grupos = models.CharField(max_length=255)  
    rol = models.CharField(max_length=50,)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    class Meta:
        db_table = 'usuarios'
        db_table_comment = 'Esta tabla almacena la información de los usuarios con sus respectivos roles y grupos.'


class UsuariosNotificaciones(models.Model):
    usuarios_notificaciones_id = models.IntegerField(db_column='Usuarios_Notificaciones_id', blank=True, null=True) 
    usuario_id = models.IntegerField(primary_key=True) 
    notificacion_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios_notificaciones'
        unique_together = (('usuario_id', 'notificacion_id'),)
        db_table_comment = 'Esta tabla establece una relacion entre usuarios y notificaciones '

class UsuariosRoles(models.Model):
    usuario_rol_id = models.AutoField(primary_key=True)
    usuario_id = models.IntegerField()
    rol_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios_roles'
        db_table_comment = 'Esta tabla establece una relacion entre usuarios y roles '

class ProyectosActividades(models.Model):
    proyecto_actividad_id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyectos, on_delete=models.SET_NULL, null=True)
    actividad = models.ForeignKey(Actividades, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyectos_actividades'
        db_table_comment = 'Almacena los ids de las tablas de Proyectos Y Actividades'
