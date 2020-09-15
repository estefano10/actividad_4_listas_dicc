def ejercicio_1_cargar_lista():
    nombres = []
    print('debe ingresar el nombre de 10 alumnos: ')
    for i in range(1, 11):
        nombre = str(input(f'ingrese el nombre del alumno {i}: '))
        nombres.append(nombre)

    print(nombres)



ejercicio_1_cargar_lista()



def ejercicio_2_modificar_lista():
    frutas = ['manzana', 'peras', 'durazno']
    verduras = ['acelga', 'lechuga']

    nueva= str(input('ingrese una nueva fruta: '))
    frutas.insert(2,nueva)
    print(frutas)

    print('se uniran las dos listas:')
    verduras.extend(frutas)
    print(verduras)

    print('se borrara la ultima fruta')
    frutas.pop(-1)
    print(frutas)


ejercicio_2_modificar_lista()


def ejercicio_3_ordenar_y_buscar_lista():
    frutas = [1998, 1989, 1970, 2020, 1990]
    print(frutas)

    print('se ordenara la lista de forma ascendente')
    frutas.sort()
    print(frutas)

    año = int(input('ingrese un año:'))
    print(año in frutas)

    print("1989 ocupa en la lista el lugar:", frutas.index(1989))


ejercicio_3_ordenar_y_buscar_lista()



def ejercicio_4_dicionarios():
    jugador = {'comida': 15, 'energia': 100, 'enemigos': 3}

    print(jugador.items())

    print('impresion de claves:')
    print(jugador.keys())

    nuevas_armas = {'rocas': 4, 'flechas': 5}
    jugador.update(nuevas_armas)
    print(jugador.items())

    elemento = {'amigos': 10}
    jugador.update(elemento)
    print(jugador.items())

    actualizacion = {'comida': 30}
    jugador.update(actualizacion)
    print(jugador.items())

    e = jugador.get('energia')
    print(e)



ejercicio_4_dicionarios()