import random
# Declaramos la función para ingresar los datos de los camiones
def ingresoDeDatos():
    # Definimos la variable que va a retornar la función añadir slicidn gmodulos propios y funviones str
    lista_camiones = []
    lista_tiempo = []
    lista_contTiempo = []
    lista_distancia = []
    lista_carga = []
    
    # Solicitamos el ingreso de camiones
    numeroCamion = int(input("Ingrese el número del camión (-1 para terminar): "))   

    while numeroCamion != -1:
        # Validamos que el número del camión sea positivo
        while numeroCamion < 1:
            numeroCamion = int(input("Ingrese un número de camión válido (-1 para terminar): "))            
                    
        # Solicitar y validar el tiempo
        tiempo = random.randint(1, 35)
        
        # Solicitar y validar la distancia
        distancia = random.randint(1, 99999)
        
        # Solicitar y validar la carga
        carga = random.randint(1, 32)
        
        # Usamos lista de comprensión para encontrar la posición del camión
        posiciones = [i for i in range(len(lista_camiones)) if lista_camiones[i] == numeroCamion]

        # Tomamos la primera posición si existe
        posicion = posiciones[0] if posiciones else -1
        
        # Si la posición es mayor a -1, el camión está en la lista
        if posicion != -1:
            # Sumamos en cada variable de tiempo, distancia y carga los valores que venían de la lista
            lista_tiempo[posicion] = int(lista_tiempo[posicion]) + tiempo
            lista_distancia[posicion] = float(lista_distancia[posicion]) + distancia
            lista_contTiempo[posicion] = int(lista_contTiempo[posicion]) + 1
            lista_carga[posicion] = float(lista_carga[posicion]) + carga
        else:
            # Agregamos los datos en las listas homogeneas
            lista_camiones.append(numeroCamion)
            lista_tiempo.append(tiempo)
            lista_distancia.append(distancia)
            lista_contTiempo.append(1)
            lista_carga.append(carga)
                            
        
        # Solicitamos el ingreso del próximo camión
        numeroCamion = int(input("Ingrese el número de camión (-1 para terminar) "))
    
    # Devolvemos los valores ingresados
    return lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga

