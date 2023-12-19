
from .forms import *

from django.shortcuts import render, redirect
from  .models import *
import random
import string

from django.contrib import messages


def generar_token(length=10):

    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = Usuario.objects.filter(username=username, password=password).first()

        if usuario:

            token = generar_token()
            usuario.token = token
            usuario.save()

            if usuario.tipo == 'estacionamiento':
                return redirect('estacionamiento', token=token)
            elif usuario.tipo == 'administrador':
                
                return redirect('admin', token=token)
            elif usuario.tipo == 'administracion':
                return redirect('administracion', token=token)

    return render(request, 'registration/Login.html')
def eliminarautosf(request,patente):
    
    producto = Estacionamiento.objects.get(patente=patente)
    producto.delete()
    
    messages.success(request, 'Auto Eliminado con éxito')  
    return redirect('lista',generar_token())





def estacionamiento(request, token):
    form = FormEstacionamiento()
    mostrar_boton = True  

    if request.method == 'POST':
        form = FormEstacionamiento(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Auto Registrado con éxito')  

    data = {'form': form, 'titulo': 'Ingresar Autos', 'mostrar_boton': mostrar_boton }
    return render(request, 'Estacionamiento/Estacionamiento.html', data)






def listaautos(request, token):
    form = FormFiltroEstacionamiento()
    if request.method == 'POST':
        form = FormFiltroEstacionamiento(request.POST)
        if form.is_valid():
            patente = form.cleaned_data.get('patente', '')
            lista_autos = Estacionamiento.objects.all()
            if patente:
                lista_autos = lista_autos.filter(patente__icontains=patente)
            data = {'token': token, 'form': form, 'patente':patente, 'Estacionaminto': lista_autos}
            return render(request, 'Estacionamiento/Datos.html', data)
        
    data = {'token': token, 'form': form, 'Estacionaminto': None}
    return render(request, 'Estacionamiento/Datos.html', data)
    
def editarautosf(request, patente):
    per = Estacionamiento.objects.get(patente=patente)
    if request.method == 'POST':
        form = FormEstacionamiento(request.POST, instance=per)
        if form.is_valid():
            form.save()
            return redirect('lista', generar_token())
    else:
        form = FormEstacionamiento(instance=per)
        form.fields['patente'].widget.attrs['readonly'] = True  

    data = {'form': form, 'titulo': 'Modificar Registro'}
    return render(request, 'Estacionamiento/Estacionamiento.html', data)








def solicitud(request):
    if request.method == 'POST':
        rut = request.POST.get('username')
        nueva_contrasena = request.POST.get('nueva')


        nueva_solicitud = Solicitud(rut=rut, nueva=nueva_contrasena)
        nueva_solicitud.save()
        return redirect('login')  

    return render(request, 'registration/forgot.html') 




def admin(request,token):

    return render(request,'Admin/Admin.html')










def eliminarpersof(request,rut):
    
    rut = Administracion.objects.get(rut=rut)
    rut.delete()
    
    messages.success(request,'Eliminado Con Exito')
    return redirect('lista.perso',generar_token())



def administracion(request,token):
    form = FormAdministracion()
    mostrar_boton = True 
    if request.method == 'POST':
        form = FormAdministracion(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Persona agregada')

    data = {'form':form,'titulo1':'Ingresar Personas','mostrar_boton': mostrar_boton }
    return render(request,'Administracion/Administracion.html',data)

def listaperso(request, token):
    form = FormFiltroAdministracion()
    if request.method == 'POST':
        form = FormFiltroAdministracion(request.POST)
        if form.is_valid():
            rut = form.cleaned_data.get('rut', '')
            lista_perso = Administracion.objects.all()
            if rut:
                lista_perso = lista_perso.filter(rut__icontains=rut)

            data = {'token': token,'form': form, 'rut': rut, 'Administracion': lista_perso}
            return render(request, 'Administracion/Datos.html', data)

    data = {'token': token,'form': form, 'Administracion': None}
    return render(request, 'Administracion/Datos.html', data)



    
def editarpersof(request,rut):
    per = Administracion.objects.get(rut=rut)
    form = FormAdministracion(instance=per)
    if request.method == 'POST':
        form = FormAdministracion(request.POST,instance=per)
        if form.is_valid():
            form.save()
            return redirect('lista.perso', generar_token() )
        
    else:
        form = FormAdministracion(instance=per)
        form.fields['rut'].widget.attrs['readonly'] = True  
    data = {'form':form,'titulo1':'Modificar Personas'}
    return render (request,'Administracion/Administracion.html',data)






def listaadperso(request, token):
    form = FormFiltroAdministracion()

    if request.method == 'POST':
        form = FormFiltroAdministracion(request.POST)
        
        if form.is_valid():
            rut = form.cleaned_data.get('rut', '')

            lista_perso = Administracion.objects.all()
            if rut:
                lista_perso = lista_perso.filter(rut__icontains=rut)

            data = {'token': token,'form': form, 'rut': rut, 'Administracion': lista_perso}
            return render(request, 'Administracion/Datos.html', data)

    data = {'token': token,'form': form, 'Administracion': None}
    return render(request, 'Administracion/Datos.html', data)




def editarpersadof(request,rut):
    per = Administracion.objects.get(rut=rut)
    form = FormAdministracion(instance=per)
    if request.method == 'POST':
        form = FormAdministracion(request.POST,instance=per)
        if form.is_valid():
            form.save()
            return redirect('persoad', generar_token() )
    data = {'form':form,'titulo1':'Modificar Personas'}
    return render (request,'Administracion/Administracion.html',data)


def eliminarpersadof(request,rut):
    
    rut = Administracion.objects.get(rut=rut)
    rut.delete()
    
    messages.success(request,'Eliminado Con Exito')
    return redirect('persoad',generar_token())




def signup(request,token):
    form = FormAdmin()
    mostrar_boton = True 
    if request.method == 'POST':
        form = FormAdmin(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Persona agregada')

    data = {'form2':form,'titulo2':'Ingresar Personas','mostrar_boton': mostrar_boton }
    return render(request,'Signup/Signup.html',data)




def listaadpersonas(request, token):
    form = FormFiltroAdmin()
    

    if request.method == 'POST':
        form = FormFiltroAdmin(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username', '')

            lista_per = Usuario.objects.all()
            if username:
                lista_per = lista_per.filter(username__icontains=username)

            data = {'token': token,'form': form, 'username': username, 'Usuario': lista_per}
            return render(request, 'Signup/Datos.html', data)

    data = {'token': token,'form': form, 'Usuario': None}
    return render(request, 'Signup/Datos.html', data)




def editarpersonas(request,username):
    per = Usuario.objects.get(username=username)
    form = FormAdmin(instance=per)
    if request.method == 'POST':
        form = FormAdmin(request.POST,instance=per)
        if form.is_valid():
            form.save()
            return redirect('pers', generar_token() )
    else:
        form = FormAdmin(instance=per)
        form.fields['username'].widget.attrs['readonly'] = True  
    data = {'form2':form,'titulo2':'Modificar Personas'}
    return render (request,'Signup/Signup.html',data)


def eliminarpersonas(request,username):
    
    rut = Usuario.objects.get(username=username)
    rut.delete()
    
    messages.success(request,'Eliminado Con exito')
    return redirect('pers',generar_token())





def listasoli(request, token):
    form = FormFiltroSoli()

    if request.method == 'POST':
        form = FormFiltroSoli(request.POST)
        
        if form.is_valid():
            rut = form.cleaned_data.get('rut', '')

            lista_perso = Solicitud.objects.all()
            if rut:
                lista_perso = lista_perso.filter(rut__icontains=rut)

            data = {'token': token,'form': form, 'rut': rut, 'Solicitud': lista_perso}
            return render(request, 'registration/Datos.html', data)

    data = {'token': token,'form': form, 'Solicitud': None}
    return render(request, 'registration/Datos.html', data)



def eliminarsoli(request,rut):
    
    rut = Solicitud.objects.get(rut=rut)
    rut.delete()
    
    messages.success(request,'Eliminado Con Exito')
    return redirect('cosa',generar_token())



