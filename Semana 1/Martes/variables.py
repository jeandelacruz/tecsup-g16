## Las variables solo pueden ser nombrados con letras, no alafnumericos ni numericos
### Formato: Snakecase
# nombre_de_variable
# No utilizar nombres de variables reservadas, para el uso general
## main -> jamás en la vida se usa

# Variables de texto
nombre = "Carlos"
apellidos = "De la cruz"
texto = """
Buenos dias:
    La carta redactada....
    .......
"""

# Hola, como estas? es tarde por alla? buenas noches
texto_en_linea = (
    "Hola, como estas? "
    "es tarde por alla? "
    "buenas noches"
)

# Operadores de salida -> console.log <-> print
# print(nombre)
# print(texto)
# print(texto_en_linea)

# Variables numericos
numero_entero = 10
numero_decimal = 10.50

## Concatenación
# print(nombre + apellidos)
# print(nombre, apellidos)
# f-string
# print(f"{nombre} {apellidos}")

# Dinamismo
# type -> nos va a retornar el tipo de variable
# print(type(nombre))
# print(type(numero_entero))
# print(type(numero_decimal))

nombre = 1500
# print(type(nombre))

# function nombre() -> salida
# function nombre_completo(nombre, apellido) -> str { return `${nombre} ${apellido}` }

# Variables booleanas
# true y false -> 1 y 0
verdadero = True
falso = False

# Definimos una variable con valor nulo
# null
variable_nulo = None

## Asignación Multiple
#persona = "Juan"
#nacionalidad = "Peruano"
persona, nacionalidad = "Juan", "Peruano"
print(persona, nacionalidad)
