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
        
        #Solicitamos el ingreso del consumo de nafta
        nafta = float(input("Ingrese el consumo de nafta en litros: "))
        #Validamos que el consumo ingresado sea correcto
        while nafta <= 0:
            nafta = float(input("El consumo de nafta debe ser mayor a 0. Ingrese el consumo de nafta en litros: "))
        
        #Validamos que la camion no este previamente en la lista
        posicion = -1
        
        #Recorremos la lista de camiones que hay hasta el momento para validar si el camion ya se ingreso
        largo = len(camiones)
        for i in range(largo):
            camion = camiones[i]
            if numeroCamion == camion[0]:
                #Guardamos la posicion de la lista para obtener los datos
                posicion = i
        
        #Si posicion es mayor a -1, el camion esta en lista
        if posicion != -1:
            #Sumamos en cada variable de tiempo, distancia y carga los valores que venian de la lista
            tiempo = int(camiones[posicion][1]) + tiempo
            contTiempo = int(camiones[posicion][1]) + 1
            distancia = float(camiones[posicion][3]) + distancia
            carga = float(camiones[posicion][4]) + carga
            nafta = float(camiones[posicion][5]) + nafta
            #Eliminamos el camion de la lista porque despues se agrega con los datos actualizados
            camiones.pop(posicion)
                            
        #Agregamos los datos en la lista
        camiones.append([numeroCamion, tiempo, contTiempo, distancia, carga, nafta])
        
        #Solicitamos el ingreso del proximo camion
        numeroCamion = int(input("Ingrese el número de camión (-1 para terminar) "))   
    
    #Devolvemos los valores ingresados
    return camiones

#Llamamos a la funcion, que va a devolver la lista de los datos ingresados
camiones = ingresoDeDatos()

#Usamos sort para ordenar la lista con la carga de toneladas
camiones.sort(key=lambda x: x[4])
        
#Imprimimos la información de los camiones ordenados
print("Camion  Tiempo promedio    Distancia recorrida      Carga Total      Promedio de Carga     Consumo por KM")
for i in range(len(camiones)):
    #Obtenemos el vector del camion
    camion = camiones[i]
    
    #Calculamos el tiempo promedio en horas
    promedioTiempoHoras = camion[1] / camion[2]
    
    #Transformamos en dias y horas
    dias = int(promedioTiempoHoras // 24)
    horas = int(promedioTiempoHoras % 24)
    
    #Calculamo el consumo de combustible por kilómetro recorridos
    consumoKilometro = camion [5] / camion [3]
    
    #Promedio de carga transportada por viaje
    promedioCarga = camion[4] / camion[2]
    
    #Si algún camión recorrió en total más de 20000 km deberá ser retirado de servicio para someterlo a una revisión mecánica.
    revisionMecanica = ""
    if camion[3] > 20000:
        revisionMecanica = "Revisión mecánica"
        
    #Mostramos los valores
    print(f"{camion[0]}         {dias}d {horas}h                    {camion[3]} km               {camion[4]} Tn          {promedioCarga} Tn/Viaje           {consumoKilometro} KM/L       {revisionMecanica}")
