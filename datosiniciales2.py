datossIniciales2 = json.loads("""
{
  "servicios" : {
    "s1" : {
      "costeinterno" : 50,
      "descripcion" : "tintoreria ",
      "jefe" : {
        "incorporacion" : "1996-10-23",
        "nombre" : "Luisa Blanco Baroja",
        "numreg" : 1,
        "sueldo" : 1000
      }
    },
    "s2" : {
      "costeinterno" : 30,
      "descripcion" : "plancha        ",
      "numreg" : 2
    },
    "s3" : {
      "costeinterno" : 60,
      "descripcion" : "lavanderia     ",
      "numreg" : 3
    },
    "s4" : {
      "costeinterno" : 15,
      "descripcion" : "bar            ",
      "numreg" : 4
    },
    "s5" : {
      "costeinterno" : 50,
      "descripcion" : "restaurante    ",
      "numreg" : 8
    },
    "s6" : {
      "costeinterno" : 25,
      "descripcion" : "floristeria    ",
      "numreg" : 9
    } 
  },
  "clientes" : {
    "111111" : {
      "apellidos" : "Aguirre",
      "domicilio" : "Pez 20, 1º A                  ",
      "nombre" : "Antonio",
      "telefono" : "999418768",
      "servicios" : {
        "1" : true,
        "5" : true
      }
    },
    "222222" : {
      "apellidos" : "Anguiano López",
      "domicilio" : "Churruca 2, 6º D              ",
      "nombre" : "Jorge",
      "telefono" : "999876737"
    } 
  }
}
""")

# Inicializacion de aplicacion
#datos = db.reference('hotel')

#metodo llenar datos SET
#datos.set(datosIniciales)

#metodo obtener datos GET
#print(datos.get())