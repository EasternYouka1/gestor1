from django.urls import path,include
from Usuarios import views

urlpatterns = [
    ######Maneja el inicio de sesion
    path('accounts/', include('django.contrib.auth.urls')),
    #####
   
    path('', views.login, name='login'),
    #Modulo Parking
    path('estacionamiento/<str:token>/', views.estacionamiento, name='estacionamiento'),
    path('estacionamiento/<str:token>/Datos', views.listaautos, name='lista'),
    path('eliminarautosf/<str:patente>',views.eliminarautosf),
    path('editarautosf/<str:patente>',views.editarautosf),


    #Url Administracion
    path('administracion/<str:token>/', views.administracion, name='administracion'),
    path('administracion/<str:token>/Datos', views.listaperso, name='lista.perso'),
    path('eliminarpersonasf/<str:rut>',views.eliminarpersof),
    path('editarpersonasf/<str:rut>',views.editarpersof),
    #Url admin
    path('admin/<str:token>/', views.admin, name='admin'),
    path('solicitud/', views.solicitud, name='solicitud'),
    path('admin/<str:token>/Datos', views.listaadperso, name='persoad'),
    path('editarpersonasadf/<str:rut>',views.editarpersadof),
    path('eliminarpersonasadf/<str:rut>',views.eliminarpersadof),


    path('admin/<str:token>/Datos1', views.listaautos, name='autoad'),

    path('admin/<str:token>/signup/', views.signup, name='signup'),
    path('eliminarpersonas/<str:username>',views.eliminarpersonas),
    path('editarpersonas/<str:username>',views.editarpersonas),
    path('admin/<str:token>/signup/Datos2', views.listaadpersonas, name='pers'),


    path('admin/<str:token>/Datos3', views.listasoli, name='cosa'),
    path('eliminarsol/<str:rut>',views.eliminarsoli),
]
