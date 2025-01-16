from django.contrib import admin
from django.urls import path,include
from principal.views import *
from principal.views1 import *
from principal.views2 import *
from principal.views3 import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
path('admin/', admin.site.urls),
path('principal/',  include(('principal.urls','principal'))),
path('principal1/', include(('principal.urls1','principal1'))),
path('principal2/', include(('principal.urls2','principal2'))),
path('principal3/', include(('principal.urls3','principal3'))),
path('home/',home, name= 'index'),
path('', LoginView.as_view(template_name='login.html'), name="login"),
path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
path('registro/', SignUpView.as_view(template_name='register.html'), name='registro'),
path('perfil/', Perfil, name= 'perfil'),
path('parametro/', parametros, name= 'indexparametro'),
path('general/', Parametros1, name= 'general'),
path('Otros/', Parametros2, name= 'Otros'),
path('Home1', Home1, name= 'index1'),
path('Contacto/',Contacto, name= 'contacto'),
path('La_fundacion/', La_fundacion, name= 'La_fundacion'),
path('Listados/', Parametros3, name= 'Listados'),
path('buscar/', buscar_en_todas_las_tablas, name='buscar'),
]