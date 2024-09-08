# Declaramos la función para ingresar los datos de los camiones
def ingresoDeDatos():
    # Definimos la variable que va a retornar la función añadir slicidn gmodulos propios y funviones str
    camiones = []
    
    # Solicitamos el ingreso de camiones
    numeroCamion = int(input("Ingrese el número no puede ser negativo (-1 para terminar) "))
    while numeroCamion < -1:
        numeroCamion = int(input("Ingrese un número de camión valido (-1 para terminar) "))
    # Solicitamos el ingreso de camiones hasta que ingrese (-1)
    while numeroCamion != -1:
        # Contamos la cantidad de veces que se ingresó el mismo camión para luego hacer el promedio de tiempo
        contTiempo = 1
        
        # Solicitamos el ingreso de tiempo        
        tiempo = int(input("Ingrese el tiempo empleado (horas) "))
        # Validamos que el tiempo ingresado sea correcto
        while tiempo <= 0:
            tiempo = int(input("El tiempo debe ser mayor a 0. Ingrese el tiempo empleado (horas) "))
            
        # Solicitamos el ingreso de la distancia
        distancia = float(input("Ingrese la distancia recorrida (km) "))
        # Validamos que la distancia ingresada sea correcta
        
        while distancia <= 0:
            distancia = float(input("La distancia debe ser mayor a 0. Ingrese la distancia recorrida (km) "))
        
        # Solicitamos el ingreso de la carga
        carga = float(input("Ingrese la carga transportada (toneladas) "))
        # Validamos que la carga ingresada sea correcta
        while carga <= 0 or carga >=32:
            carga = float(input("La carga total debe ser mayor a 0 y menor o igual a 32. Ingrese la carga transportada (toneladas) "))

        # Usamos lista de comprensión para encontrar la posición del camión
        posiciones = [i for i in range(len(camiones)) if camiones[i][0] == numeroCamion]

        # Tomamos la primera posición si existe
        posicion = posiciones[0] if posiciones else -1
        
        # Si la posición es mayor a -1, el camión está en la lista
        if posicion != -1:
            # Sumamos en cada variable de tiempo, distancia y carga los valores que venían de la lista
            tiempo = int(camiones[posicion][1]) + tiempo
            contTiempo = int(camiones[posicion][2]) + 1
            distancia = float(camiones[posicion][3]) + distancia
            carga = float(camiones[posicion][4]) + carga
            # Eliminamos el camión repetido de la lista porque después se agrega con los datos actualizados
            camiones = camiones[:posicion] + camiones[posicion+1:]
                            
        # Agregamos los datos en la lista
        camiones.append([numeroCamion, tiempo, 1, distancia, carga])
        
        # Solicitamos el ingreso del próximo camión
        numeroCamion = int(input("Ingrese el número de camión (-1 para terminar) "))  
    
    # Devolvemos los valores ingresados
    return camiones