#EJERCICIO1
#INDICAR VALORES
distancia1=float(input("INGRESE UNA DISTANCIA EN PIES:"))
distancia2=float(input("INGRESE UNA DISTANCIA EN PULGADAS:"))

#CONVERTIMOS
conversion1=((distancia1*12)* 2.54)
conversion2=(distancia2* 2.54 )

#AHORA IMPRIMIR
print("La distancia1 en centimetros es:" ,(conversion1))
print("La distancia2 en centimetros es:" ,(conversion2))




#EJERCICIO2
#INDICAR VALORES
temperatura=float(input("INGRESE LA TEMPERATURA(GRADOS FAHRENHEIT): "))

#CONVERSION DE CELSIUS A FAHRENHEIT
temperatura_grados_celsius=(((5*temperatura)-160)/9)

#AHORA IMPRIMIR
print("LA TEMPERATURA EN CELSIUS ES: ", (temperatura_grados_celsius))