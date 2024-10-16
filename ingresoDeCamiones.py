import random

# Función que solicita el número del camión y llama a la función de identificación
def ingreso_camion(lista_camiones, camiones_data, cargas_data):
    # Solicitar el número de camión
    numeroCamion = input("Ingrese el número del camión (-1 para terminar): ")
    
    # Condición base para terminar el ciclo
    if numeroCamion == "-1":
        print("Se terminó la entrada de camiones.")
        return lista_camiones, camiones_data, cargas_data
    
    try:
        numeroCamion = int(numeroCamion)

        # Validar que el número de camión sea positivo
        if numeroCamion < 1:
            print("Por favor, ingrese un número de camión válido.")
        else:
            # Llamar a la función de identificación
            ingreso_identificacion(numeroCamion, camiones_data, cargas_data)

            # Añadir el camión a la lista si no está registrado
            if numeroCamion not in lista_camiones:
                lista_camiones.append(numeroCamion)

    except ValueError:
        print("Por favor, ingrese un número de camión válido.")
    
    # Volver a pedir otro camión después de procesar la identificación
    return ingreso_camion(lista_camiones, camiones_data, cargas_data)


# Función que solicita la identificación del camión y almacena los datos
def ingreso_identificacion(numeroCamion, camiones_data, cargas_data):
    # Solicitar el número de identificación
    identificacion = input(f"Ingrese una identificación para el camión {numeroCamion}: ")
    
    try:
        identificacion = int(identificacion)

        # Validar que la identificación sea positiva
        if identificacion < 0:
            print("Por favor, ingrese un número de identificación válido.")
            ingreso_identificacion(numeroCamion, camiones_data, cargas_data)  # Reintentar si la identificación no es válida
        else:
            # Solicitar y validar el tiempo, distancia y carga
            tiempo = random.randint(1, 35)
            distancia = random.randint(1, 99999)
            carga = random.randint(1, 32)

            # Agregar o actualizar datos del camión
            if numeroCamion not in camiones_data:
                camiones_data[numeroCamion] = {
                    'tiempo': tiempo,
                    'distancia': distancia,
                    'contTiempo': 1
                }
                cargas_data[numeroCamion] = [(identificacion, carga)]  # Inicializar carga
            else:
                camiones_data[numeroCamion]['tiempo'] += tiempo
                camiones_data[numeroCamion]['distancia'] += distancia
                camiones_data[numeroCamion]['contTiempo'] += 1
                cargas_data[numeroCamion].append((identificacion, carga))  # Agregar carga

            print(f"Camión {numeroCamion} con identificación {identificacion} registrado correctamente.")

    except ValueError:
        print("Por favor, ingrese un número de identificación válido.")
        ingreso_identificacion(numeroCamion, camiones_data, cargas_data)  # Volver a intentar si la conversión falla


# Función para iniciar la carga de datos de los camiones
def ingresoDeDatos():
    lista_camiones = []
    camiones_data = {}  # Diccionario para almacenar los datos de cada camión
    cargas_data = {}    # Diccionario para almacenar las cargas de cada camión

    # Iniciar el ciclo de ingreso de camiones
    lista_camiones, camiones_data, cargas_data = ingreso_camion(lista_camiones, camiones_data, cargas_data)

    # Devolvemos los valores ingresados
    lista_tiempo = [camiones_data[camion]['tiempo'] for camion in lista_camiones]
    lista_distancia = [camiones_data[camion]['distancia'] for camion in lista_camiones]
    lista_contTiempo = [camiones_data[camion]['contTiempo'] for camion in lista_camiones]
    lista_carga = [cargas_data[camion] for camion in lista_camiones]

    return lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga


# Llamar a la función principal para comenzar el proceso
lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga = ingresoDeDatos()

# Puedes imprimir las listas para verificar los resultados
print("Camiones:", lista_camiones)
print("Tiempos:", lista_tiempo)
print("Distancias:", lista_distancia)
print("Contadores de Tiempo:", lista_contTiempo)
print("Cargas:", lista_carga)
