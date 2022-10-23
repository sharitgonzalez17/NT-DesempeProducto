#Contruir un programa que permita ingresar N (Cantidad digitada por
# el usuario) nùmerps enteros y cuente cuantos mùltiplos de 2 y 3 
# fueron ingresados(+1)
 
from itertools import count


saltos = int(input("DIGITA LA CANTIDAD DE SALTOS QUE DESEA DAR: "))
count = 0
num1 = 0
num2 = 0

for x in range (saltos):
    numero= int (input("Ingresa Un Numero: "))
    if(numero % 2 ==0):
        num1 += 1
    elif(numero % 3 ==0):
        num2 += 1

print(f"{num1} son multiplos de 2")
print(f"{num2} aon multiplos de 3")