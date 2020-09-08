# modulos de autenticacion y firebase
from firebase_admin import initialize_app
from firebase_admin import credentials
from firebase_admin import db
import json

# Ruta credencial fire base
cred = credentials.Certificate("clave3.json")
initialize_app(cred, {
    'databaseURL': 'https://hotel-2121b.firebaseio.com'
    })



# 1) Obtener un listado de los empleados del hotel, con todos sus datos.
datos = db.reference('hotel/empleado')
empleados = datos.get()
print("\n EMPLEADOS HOTEL\n")
#recorrer datos objeto diccionario
for key, val in empleados.items():
    print(f"Cod: {key}, {val}")

print("\n-------------------------------------------------------\n")

# 2) Obtener el nombre del jefe del servicio de "Restaurante"
# obtener servicio Restaurante
datos = db.reference('hotel/servicio')
servicios = datos.order_by_child("descripcion").equal_to("restaurante").get()
#print(servicios.items())
for key, val in servicios.items():
    codjefe = val.get("empleado") 
    codjefe = "numreg"+str(codjefe)   
    break
# obtener nombre del jefe del servicio
datos = db.reference('hotel/empleado')
empleado = datos.get().get(codjefe)
#imprimir objeto empleado
print(f"Empleado:{codjefe}, {empleado}")
#imprimir nombre empleado
print("El jefe de restaurante es:", empleado["nombre"])

print("\n-------------------\n")




# 3) Obtener el nombre del jefe de "Jorge Alonso Alonso".

# Obtener empleado Jorge
datos = db.reference('hotel/empleado')
#ordenar por clcave
#print(datos.get())
#obntener subcampo de la clave
empleado = datos.order_by_child("nombre").equal_to("Jorge Alonso Alonso").get()
# Obtener valor del objeto Jorge
for key, val in empleado.items():
    servicio = val["cods"]
    # llave servicio de Jorge
    servicio = "s"+str(servicio)
    break
# obtener servicios
datos = db.reference('hotel/servicio')
servicios = datos.get()
#print(servicios.items())
#print(datos.get())
# obtener servicio de jorge
servicio = servicios.get(servicio)
# obtener el id del jefe del servicio de Jorge
codjefe = servicio["empleado"]
codjefe = "numreg"+str(codjefe)
# obtener servicio del jefe de Jorge
datos = db.reference('hotel/empleado')
jefe = datos.get().get(codjefe)
print("El jefe de Jorge es:", jefe["nombre"])

print("\n-------------------\n")

# 4) Obtener un listado de los empleados y los servicios a los que están asignados, 
# exclusivamente para aquellos que tengan algún servicio asignado.
# obtener servicios

listado = []
datos = db.reference('hotel/servicio')
servicios = (datos.order_by_child("empleado").get()).values()
for s in servicios:
    codemp = s["empleado"]
    codemp = "numreg"+str(codemp)
    datos = db.reference('hotel/empleado')
    empleado = (datos.get().get(codemp))["nombre"]
    servicio = s["descripcion"]
    listado.append((empleado, servicio))
# obtener empleados
datos = db.reference('hotel/empleado')
empleados = datos.order_by_child("cods").get()
print("Empleados asignados un servicio")
for key, emp in empleados.items():
    if "cods" in emp:
        empleado = emp["nombre"]
        codser = "s"+str(emp["cods"])
        datos = db.reference('hotel/servicio')
        servicio = (datos.get().get(codser))["descripcion"]
        tupla = (empleado, servicio)
        if tupla not in listado:
            listado.append(tupla)
for item in listado:
    print(f"Empleado: {item[0]}     Servicio: {item[1]}")
    


# 7) Obtener los datos del empleado o empleados que hayan limpiado 
# todas las habitaciones del hotel

# obtener listado de numeros de habitaciones
datos = db.reference('hotel/habitacion')
habitaciones = datos.get()
#obtener lista claves objetos
codhabitaciones = list(habitaciones.keys())
#print(habitaciones.keys())
# obtener limpiezas
datos = db.reference('hotel/limpieza')
#obtener datos lipieza en lista
limpiezas = list((datos.get()).values())
#print(datos.get().values())
# recorrer registros
print("Empleados que limpiaron todas las habitaciones")
empleados = dict()#crear diccionario
for lim in limpiezas:
    if(lim["empleado"] not in empleados.keys()):
        empleados[lim["empleado"]] = [str(lim["habitacion"])]
    else:
        if(str(lim["habitacion"]) not in empleados[lim["empleado"]]):
            empleados[lim["empleado"]].append(str(lim["habitacion"]))
for key, val in empleados.items():
    if(set(val)==set(codhabitaciones)):
        cod = "numreg"+str(key)
        datos = db.reference('hotel/empleado')
        empleado = datos.get().get(cod)
        print(f"Cod: {cod}, {empleado}")

print("\n-------------------\n")

