## Ejercicio
# Crear un programa que te permita ingresar 6 números de los cuales
# si uno tiene un formato incorrecto, nos va a indicar un mensaje de error
# pero los que si tengan el formato correcto, se agregaran en una lista
# al final nos retornara la lista con los números correctos
numeros = []

for _ in range(6):
    try:
        numero = int(input('Ingrese el número: '))
        numeros.append(numero)
    except Exception:
        print('El número ingresado es incorrecto')
        
print(numeros)

