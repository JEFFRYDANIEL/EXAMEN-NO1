#EJERCICIO3
#INDICAR VALORES
año_actual=int(input("INGRESAR EL AÑO ACTUAL: "))
año_cualquiera=int(input("INGRESAR UN AÑO CUALQUIERA: "))

if año_actual > año_cualquiera:
    años_faltantes=(año_actual-año_cualquiera)
    print("HA PASADO " + str(años_faltantes) +" AÑOS ")

elif año_actual < año_cualquiera:
    años_faltantes=(año_cualquiera-año_actual)
    print("FALTAN " + str(años_faltantes) +" AÑOS ")
else:
    print("LOS AÑOS SON IGUALES")
#fin



#EJERCICIO4
#INDICAR VALORES
opcion=input("ELEGIR EL AREA DE LA FIGURA GEOMETRICA QUE QUIERE HALLAR(TRIANGULO/CIRCULO): ")

if opcion=="C" or opcion=="c":
    radio=float(input("INGRESE EL RADIO: "))
    area_circulo=(3.14*(radio*radio))
    print("EL AREA DEL CIRCULO ES:", (area_circulo))

elif opcion=="T" or opcion=="t":
    base=float(input("INGRESE LA BASE: "))
    altura=float(input("INGRESE LA ALTURA: "))
    area_tringulo=((base*altura)/2)
    print("EL AREA DEL TRIANGULO ES:", (area_tringulo))

else:
    print("INGRESE UNA OPCION CORRECTA")
#fin