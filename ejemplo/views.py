#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Mascota, Vehiculo
from ejemplo.forms import Buscar, Buscar_Mascota, Buscar_Vehiculo
from django.views import View 
from ejemplo.forms import FamiliarForm 
from ejemplo.forms import MascotaForm
from ejemplo.forms import VehiculoForm


#def index(request,nombre):
#    return render(request, "ejemplo/saludar.html")

"""def saludar_a(request,nombre):
    return render(request, 
    "ejemplo/saludar_a.html",
    {"nombre": nombre}
    )

def sumar(request, a, b):
    return render(request, 
    "ejemplo/sumar.html",
    {"a": a,
    "b": b,
    "resultado": a + b
    }
    )"""

"""def buscar(request):
    lista_de_nombre = ["German", "Daniel", "Romero", "Alvaro"]
    query = request.GET['q']
    if query in lista_de_nombre:
        indice_de_resultado = lista_de_nombre.index(query)
        resultado= lista_de_nombre[indice_de_resultado]
    else:
        resultado="No hay match"
    return render(request, 'ejemplo/buscar.html', {"resultado": resultado})
    
"""

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}


    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class ActualizarFamiliar(View):
    form_class = FamiliarForm
    template_name = 'ejemplo/actualizar_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(instance=familiar)
        return render(request, self.template_name, {'form':form,'familiar': familiar})

    # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(request.POST ,instance=familiar)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
        return render(request, self.template_name, {"form": form})

class BorrarFamiliar(View):
    template_name = "ejemplo/familiares.html"
    
  
    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        familiar.delete()
        familiares= Familiar.objects.all()
        return render(request, self.template_name, {'lista_familiares': familiares})

#********
"""

def mascotas(request):
    lista_de_nombre = ["German", "Daniel", "Romero", "Alvaro"]
    query = request.GET['q']
    if query in lista_de_nombre:
        indice_de_resultado = lista_de_nombre.index(query)
        resultado= lista_de_nombre[indice_de_resultado]
    else:
        resultado="No hay match"
    return render(request, 'ejemplo/buscar.html', {"resultado": resultado})
#**************************
"""

def mostrar_mascota(request):
    lista_mascotas = Mascota.objects.all()
    return render(request, "ejemplo/mascotas.html", {"lista_mascotas": lista_mascotas})


class BuscarMascota(View):
    form_class = Buscar_Mascota
    template_name = 'ejemplo/buscar_mascota.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascotas = Mascota.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas':lista_mascotas})
        return render(request, self.template_name, {"form": form})

class AltaMascota(View):

    form_class = MascotaForm
    template_name = 'ejemplo/alta_mascota.html'
    initial = {"animal":"", "nombre":"", "dueno":""}


    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})



class ActualizarMascota(View):
    form_class = MascotaForm
    template_name = 'ejemplo/actualizar_mascota.html'
    initial = {"animal":"", "nombre":"", "dueno":""}
  
    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        mascota = get_object_or_404(Mascota, pk=pk)
        form = self.form_class(instance=mascota)
        return render(request, self.template_name, {'form':form,'mascota': mascota})

    # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk): 
        mascota = get_object_or_404(Mascota, pk=pk)
        form = self.form_class(request.POST ,instance=mascota)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                      'mascota': mascota,
                                                      'msg_exito': msg_exito})
      
        return render(request, self.template_name, {"form": form})

class BorrarMascota(View):
    template_name = "ejemplo/mascotas.html"
    
  
    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        mascota = get_object_or_404(Mascota, pk=pk)
        mascota.delete()
        mascota= Mascota.objects.all()
        return render(request, self.template_name, {'lista_mascotas': mascota})



####  comienza vehiculos



def mostrar_vehiculo(request):
    lista_vehiculo = Vehiculo.objects.all()
    return render(request, "ejemplo/vehiculo.html", {"lista_vehiculo": lista_vehiculo})

class BuscarVehiculo(View):
    form_class = Buscar_Vehiculo
    template_name = 'ejemplo/buscar_vehiculo.html'
    initial = {"titular":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            titular = form.cleaned_data.get("titular")
            lista_vehiculo = Vehiculo.objects.filter(titular__icontains= titular).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_vehiculo':lista_vehiculo})
        return render(request, self.template_name, {"form": form})#

class AltaVehiculo(View):

    form_class = VehiculoForm
    template_name = 'ejemplo/alta_vehiculo.html'
    initial = {"tipo":"", "marca":"", "titular":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el Vehiculo {form.cleaned_data.get('titular')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})

class ActualizarVehiculo(View):
    form_class = VehiculoForm
    template_name = 'ejemplo/actualizar_vehiculo.html'
    initial = {"tipo":"", "marca":"", "titular":""}

    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        form = self.form_class(instance=vehiculo)
        return render(request, self.template_name, {'form':form,'vehiculo': vehiculo})

    # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk): 
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        form = self.form_class(request.POST ,instance=vehiculo)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el Vehiculo {form.cleaned_data.get('tipo')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                      'vehiculo': vehiculo,
                                                      'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})

class BorrarVehiculo(View):
    template_name = "ejemplo/vehiculo.html"


    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        vehiculo.delete()
        vehiculo= Vehiculo.objects.all()
        return render(request, self.template_name, {'lista_vehiculo': vehiculo})
