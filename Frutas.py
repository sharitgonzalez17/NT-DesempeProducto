#Leer el nombre de 10 frutas {nombre, color, precio}
#para preparar un salpicòn; el programa debe permitir mostrar las 10
#frutas ingresadad al mismo tiempo  en sentido inverso al ingresado(+1)

frutas =[]

for i in range(0,11):
    fruta ={}
    fruta['Nombre']=input("Ingrese el nombre de una fruta: ")
    fruta['Color']=input("Ingrese Un Color: ")
    fruta['Precio']=input("Ingrese El Precio: ")

    frutas.append(fruta)
    frutas.reverse()
    print(f"{frutas} lista de ciudades")