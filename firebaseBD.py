# modulos de autenticacion y firebase
from firebase_admin import initialize_app
from firebase_admin import credentials
from firebase_admin import db
import json

# Ruta de la credencial
cred = credentials.Certificate("C:\\Users\\santi\\Desktop\\Python\\clave2.json")
initialize_app(cred, {
    'databaseURL': 'https://hotel-2121b.firebaseio.com'
    })

datosIniciales = json.loads(open("datosiniciales.json","r").read())

# Inicializacion de aplicacion
datos = db.reference('hotel')

#metodo llenar datos SET
datos.set(datosIniciales)

#metodo obtener datos GET
print(datos.get())