#Declaramos de la funcion, para ingresar los datos de los camiones
def ingresoDeDatos():
    
    #Definimos la variable que va retornar la funcion
    camiones = []
    
    #Solicitamos el ingreso de camiones
    numeroCamion = int(input("Ingrese el número de camión (-1 para terminar) "))
    
    #Solicitamos el ingreso de camiones hasta que ingrese (-1)
    while numeroCamion != -1:
        #Contamos la cantidad de veces que se ingreso el mismo camion para luego hacer el promedio de tiempo
        contTiempo = 1
        
        #solicitamos el ingreso de tiempo        
        tiempo = int(input("Ingrese el tiempo empleado (horas) "))
        #Validamos que el tiempo ingresado sea correcto
        while tiempo <= 0:
            tiempo = int(input("El tiempo debe ser mayor a 0. Ingrese el tiempo empleado (horas) "))
            
        #Solicitamos el ingreso de la distancia
        distancia = float(input("Ingrese la distancia recorrida (km) "))
        #Validamos que la distancia ingresada sea correcta
        while distancia <= 0:
            distancia = float(input("La distancia debe ser mayor a 0. Ingrese la distancia recorrida (km) "))
        
        #Solicitamos el ingreso de la carga
        carga = float(input("Ingrese la carga transportada (toneladas) "))
        #Validamos que la carga ingresada sea correcta
        while carga <= 0:
            carga = float(input("La carga total debe ser mayor a 0. Ingrese la carga transportada (toneladas) "))    
        
        #Validamos que la camion no este previamente en la lista
        posicion = -1
        #Recorremos la lista de camiones que hay hasta el momento para validar si el camion ya se ingreso
        largo = len(camiones)
        for i in range(largo):
            camion = camiones[i]
            if numeroCamion == camion[0]:
                #Guardamos la posicion de la lista para obtener los datos
                posicion = i
                #Cortamos el for para no seguir avanzando innecesariamente
                i = largo + 1                
        
        #Si posicion es mayor a -1, el camion esta en lista
        if posicion > -1:
            #Sumamos en cada variable de tiempo, distancia y carga los valores que venian de la lista
            tiempo = int(camiones[posicion][1]) + tiempo
            contTiempo = int(camiones[posicion][2]) + contTiempo
            distancia = float(camiones[posicion][3]) + distancia
            carga = float(camiones[posicion][4]) + carga
            #Eliminamos el camion de la lista porque despues se agrega con los datos actualizados
            del camiones[posicion]
                        
        #Agregamos los datos en la lista
        camiones.append((numeroCamion, tiempo, contTiempo, distancia, carga))
        
        #Solicitamos el ingreso del proximo camion
        numeroCamion = int(input("Ingrese el número de camión (-1 para terminar) "))   
    
    #Devolvemos los valores ingresados
    return camiones

#Llamamos a la funcion, que va a devolver la lista de los datos ingresados
camiones = ingresoDeDatos()

#Declaramos la funcion para ordenar de menor a mayor por carga total
def burbujeo(camiones):
    largo = len(camiones)
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(largo-1):
            if camiones[i][4] > camiones[i+1][4]:  # Cambio de > a <               
                #Intercambiar elementos en la lista de camiones
                aux = camiones[i]
                camiones[i] = camiones[i+1]
                camiones[i+1] = aux
                desordenada = True
    #Devolvemos los camiones ordenados
    return camiones

#Llamamos a la función de burbujeo para ordenar los camiones por la carga transportada
camiones = burbujeo(camiones)

#Imprimimos la información de los camiones ordenados
print("Camion    Tiempo promedio    Distancia recorrida    Carga Total")
for i in range(len(camiones)):
    #Obtenemos el vector del camion
    camion = camiones[i]
    
    #Calculamos el tiempo promedio en horas
    promedioTiempoHoras = camion[1] / camion[2]
    
    #Transformamos en dias y horas
    dias = int(promedioTiempoHoras // 24)
    horas = int(promedioTiempoHoras % 24)
    
    #Si algún camión recorrió en total más de 20000 km deberá ser retirado de servicio para someterlo a una revisión mecánica.
    revisionMecanica = ""
    if camion[3] > 20000:
        revisionMecanica = "Revisión mecánica"
    
    #Mostramos los valores
    print(camion[0],'       ', dias,'d ' , horas, 'h         ', camion[3], 'km                 ', camion[4],'Tn   ' ,revisionMecanica)