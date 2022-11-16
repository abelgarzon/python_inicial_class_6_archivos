# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con diccionarios

import csv
from termcolor import colored

def ingresar_cantidad():
    try:
        cantidad = int(input(
            'Ingrese la cantidad a agregar al producto, 0 para salir: '))
        return {"unidades": cantidad, "status_int": True}
    except:
        return {"status_int": False}

def desafio():
    print('--Ejercicio con diccionarios como base de datos--')
    # Utilizaremos el diccionario como una base de datos.
    # Comenzaremos con un diccionario de stock
    # de nuestros productos en cero:

    stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0}

    # Paso 1:
    # Crear un bucle utilizando while que se ejecute de forma infinita
    while True:

    # Paso 2:
    # Dentro de ese bucle consultar al usuario por consola
    # que producto desea agregar al stock

        end = False
        producto_existe = False

        producto = input(
            '\nIngrese el producto que desea agregar al stock, FIN para salir: ')
        producto = producto.lower()

    #   - Si el usuario ingresa "FIN" como producto se debe
    #   finalizar el bucle
        if producto == 'fin' or end == True: break

    #   - No debe agregar stock de productos que no estén
    #   definidos inicialmente en el diccionario stock.
    #   Para verificar si un producto existe dentro del
    #   diccionario stock utilice el operador "in" visto en clase

        for elemento in stock:
            if elemento == producto:

    # Paso 3:
    # Luego de haber ingresado el producto valido, se debe
    # ingresar por consola cuanto stock de ese producto se desea agregar.
    # Si teniamos 20 tornillos y el usuario desea agregar 10 tornillos más,
    # en nuestro diccionario deben quedar 30 tornillos (debe acumular)

                producto_existe = True
                cantidad = ingresar_cantidad()
                if cantidad["status_int"] == True:
                    if cantidad["unidades"] == 0:
                        end = True
                        break
                    else: stock[elemento] += cantidad["unidades"]
                else:
                    print(colored('Debe ingresar un número entero!!!',
                        'yellow', attrs=["bold"]))
        if producto_existe == False:
            print(colored('El producto no se encuentra en inventario!!!',
                'magenta', attrs=["bold"]))

    # Paso 4:
    # Cuando el usuario ingrese "FIN" y se termine el bucle, debe
    # imprimir en pantalla con print el diccionario con el stock final
    # Al final de esta función retornar (return) la variable stock

    print(colored(f'\nSu inventario: {stock}', 'cyan', attrs=["bold"]))
    return stock

    # Comenzar aquí, recuerde el identado dentro de esta funcion

if __name__ == '__main__':
    print("***Bienvenidos a otra clase de Inove con Python***")
    desafio()
    print(colored('\nfin del programa', 'grey', attrs=["bold"]))


