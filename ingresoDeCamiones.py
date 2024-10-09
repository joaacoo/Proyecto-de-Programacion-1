import random

# Declaramos la función para ingresar los datos de los camiones
def ingresoDeDatos():
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
            
        identificacion = int(input("Ingrese un número de identificación: "))
        
        while identificacion < 0:
            identificacion = int(input("Ingrese un número de identificación válido: "))
   
        # Solicitar y validar el tiempo
        tiempo = random.randint(1, 35)
        
        # Solicitar y validar la distancia
        distancia = random.randint(1, 99999)
        
        # Solicitar y validar la carga
        carga = random.randint(1, 32)
        
        camion_existente = False
        
        # Verificamos si el camión ya está en la lista
        for i in range(len(lista_camiones)):
            if lista_camiones[i] == numeroCamion:
                camion_existente = True
                # Sumamos en cada variable de tiempo, distancia y carga los valores que venían de la lista
                lista_tiempo[i] += tiempo
                lista_distancia[i] += distancia
                lista_contTiempo[i] += 1
                lista_carga[i].append([identificacion, carga])  # Agregar la carga y identificación
                i = len(lista_camiones)  # Para salir del ciclo for
        
        if not camion_existente:  # Si el camión no existe
            lista_camiones.append(numeroCamion)
            lista_tiempo.append(tiempo)
            lista_distancia.append(distancia)
            lista_contTiempo.append(1)
            lista_carga.append([[identificacion, carga]])  # Inicializar con una lista que contenga [identificacion, carga]
        
        # Solicitar el ingreso del próximo camión
        numeroCamion = int(input("Ingrese el número de camión (-1 para terminar): "))
    
    # Devolvemos los valores ingresados
    return lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga