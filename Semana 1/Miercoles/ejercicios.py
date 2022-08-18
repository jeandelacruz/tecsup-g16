# Ejercicio 1
# Solicitar una palabra y validarla si esta es un palindromo
# ana -> ana
# palabra[inicio:final:paso] -1

# palabra = input("Ingrese una palabra: ")

# Solución 1
# if palabra == palabra[::-1]:
#     print('Es un palindromo')
# else:
#     print('No es un palindromo')

# Solución 2
# letras_invertidas = []
# 
# for letra in palabra:
#     letras_invertidas.insert(0, letra)
#     
# palabra_invertida = ''.join(letras_invertidas)
# 
# if palabra == palabra_invertida:
#     print('Es un palindromo')
# else:
#     print('No es un palindromo')

# Solucion 3
# palabra_invertida = ''.join(reversed(palabra))
# if palabra == palabra_invertida:
#     print('Es un palindromo')
# else:
#     print('No es un palindromo')

# Ejercicio 2
# Solicitar el año en que nacio, este mismo se va a iterar restandolo el año actual
# de tal manera nos mostraria cuantos años tenemos en cada año iterado
# 2022
# 1994
# 28
# En el año 1995, tenia 1 años
# En el año 1996, tenia 2 años
# ......
# En el año 2022, tenia 28 años
# while, input, for, if

anio_actual = 2022
anio_nacimiento = int(input('Ingrese el año en el que naciste: '))

if anio_nacimiento < anio_actual:
    edad = anio_actual - anio_nacimiento
    for i in range(edad):
        edad_anterior = i + 1
        if (anio_nacimiento + edad_anterior) == anio_actual:
            print(f'Actualmente en el año {anio_actual}, tienes {edad_anterior} años')
        else:
            print(f'En el año {anio_nacimiento + edad_anterior} tenias {edad_anterior} años')
else:
    print(f'El año de nacimiento no debe ser mayor a {anio_actual}')
