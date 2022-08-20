## function nombre() { logica }

# Función en python
#def nombreFuncion():
#    pass

# Función con parametro
def saludar(nombre):
    print(f'Hola {nombre}, como estas?')
    
# Función con parametros, con valor por defecto
def saludarConNombre(apellido, nombre="Cesar"):
    print(f'{nombre} {apellido}')
    
# saludarConNombre(nombre="Edgar", apellido="Razuri")

# Ejercicio
# Crear una función que reciba 2 números, donde el primer número tenga
# un valor por defecto: 10
# si dichos números al sumarlos es par, hallar la mitad
# y si es impar mostrar el resultado de la suma
def ejercicioUno(n2, n1=10):
    suma = n1 + n2
    if suma % 2 == 0:
        print(suma/2)
    else:
        print(suma)

# ejercicioUno(10)

# Función con multiparametros
# *args, nos ayuda para poder recibir valores infinitos como argumento, 
# dentro de la función obtenemos una tupla con los 
# valores -> nombreFuncion("Valor1", "Valor2", ....., "ValorX")
#########################################################################
# **kwargs -> nombreFuncion(valoruno="1", valordos="2", .....,valorx="x")

def alumnosInscritos(*args):
    print(args)

# alumnosInscritos("Arturo", "Cesar", "Daniel", "Christian", "David")

def cursosDeAlumnos(**kwargs):
    print(kwargs)

# cursosDeAlumnos(curso_uno="Algebra", curso_dos="Aritmetica", curso_tres="Matematica")

# Ejercicio 2
# Crea una función que reciba N notas, y te indique 
# cuantas desaprobaron y cuantas aprobaron
# nota > 10 -> Aprobado
