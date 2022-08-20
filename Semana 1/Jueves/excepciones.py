try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print('El valor ingresado no es un número')
except ZeroDivisionError:
    print('El número ingresado debe ser mayor a 0')
except KeyboardInterrupt:
    print('\nLa aplicación se cerro')
except Exception as e:
    print(e.__class__)
    print('Hay un error')
else: # Se ve a ejecutar siempre y cuando no haya un error
    print(f'No hubo un error -> {resultado}')
finally: # Se va a ejecutar al final, aunque este bien o haya un error
    print('Siempre')
