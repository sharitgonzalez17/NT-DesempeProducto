#Construir un programa para ir de compras en un supermercado que permita la construccion del siguiente MENU:
#1.Digitar 1 para recibir {còdigo,nombre,precio} de un producto (+0.4)
# 2.Digitar 2 para mostrar todos los productos registrados (+0.4)
# 3.Digitar 3 para permitir buscar por còdigo un producto y editar el precio de este (+0.4)
# 4.Digitar 4 para permitir buscar por còdigo un producto y eliminar el producto(+1.4)
  
print("***MENU***")
print("1. Agregar Producto")
print("2. Mostrar Producto")
print("3. Buscar y Editar Producto")
print("4. Buscar Y Eliminar Producto")
print("5. SALIR")
opcion = 0

productos=[]

while(opcion!=5):
    producto={}
    opcion= int(input("Digite Una Opciòn: "))
    if(opcion==1):

        producto['codigo']=input("Ingrese El Codigo Del Producto: ")
        producto['nombre']=input("Ingrese El Nombre Del Producto: ")
        producto['precio']=input("Ingrese El Precio: ")
        productos.append(producto)
        print("Agregando Productos... ")
    elif(opcion==2):
        print(productos)
        print("Mostrando Producto")

    elif(opcion==3):
        codigo = input("Ingrese El Producto Para Buscar Y Editar: ")
        for auxiliar in productos:
            if auxiliar['codigo']==codigo:
                print(auxiliar)
                auxiliar['precio'] = input("Ingrese El Precio: ")
                break
    elif(opcion==4):
        codigo = input("Ingrese El Codigo Para Buscar Y Eliminar: ")
        index=[x['codigo']for x in productos].index(codigo)
        productos.pop(index)
        print(productos)
    else:
        print("Ingrese Una Opcion Valida")
else:
    print("FIN")