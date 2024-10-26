from ingresoDeCamiones import ingresoDeDatos,guardarDatosEnCsv



def cargar_matriz_recursivo(claves, cargas_data, resultado):
    # Caso base: si no hay más claves que procesar, devolvemos el resultado final
    if not claves:
        return resultado

    # Procesamos el primer elemento en 'claves'
    numeroCamion = claves[0]
    cargas = cargas_data[numeroCamion]
    
    # Obtenemos la identificación del chofer del camión actual
    for carga in cargas:        
        identificacion = carga["identificacion"]

        # Actualizamos el conteo de viajes para cada identificación en 'resultado'
        if identificacion not in resultado:
            resultado[identificacion] = 1
        else:
            resultado[identificacion] += 1

    # Llamada recursiva para el resto de los elementos en 'claves'
    return cargar_matriz_recursivo(claves[1:], cargas_data, resultado)





def imprimirMatriz(matriz, identificaciones):
    print(f"{'Identificación':>40}")  # Centrar la palabra "Identificación"
    print(f"{'Número de Camión':>20}", end=" ")  # Alinear el encabezado "Número de Camión"
    
    
    # Imprimir los encabezados de identificación
    for iden in identificaciones:
        print(f"{iden:>20}", end=" ")  # Alinear las identificaciones
    print()  # Nueva línea


    # Imprimir la matriz
    for fila in matriz:
        for elemento in fila:
            print(f"{str(elemento):>20}", end=" ")  # Alinear a la derecha
        print()



def guardarInformes():
    # Abre el archivo de datos previamente guardado
    try:    
        try:
            arch = open("camionIden.csv", mode="r")
        except IOError:
            print("No se pudo abrir el archivo camionIden.csv para lectura.")

        try:
            distanciaArch = open("distancia.csv", mode="w")
            distanciaArch.write("Numero de Camion;Distancia Recorrida (KM); Carga traslada (Tn);Cantidad de viajes\n")
        except IOError:
            print("No se pudo crear el archivo distancia.csv.")

        try:
            tiempoPromedioArch = open("tiempoPromedio.csv", mode="w")
            tiempoPromedioArch.write('Numero de Camion;Días;Horas;Minutos\n')
        except IOError:
            print("No se pudo crear el archivo tiempoPromedio.csv.")
            

        try:
            dieselArch = open("consumoDiesel.csv", mode="w")
            dieselArch.write("Numero de Camion;Consumo de Diesel(L)\n")
        except IOError:
            print("No se pudo crear el archivo consumoDiesel.csv.")
            

        try:
            revisionMecanicaArch = open("revisionMecanica.csv", mode="w")
            revisionMecanicaArch.write("Numero de Camion;Distancia Recorrida (KM)\n")
        except IOError:
            print("No se pudo crear el archivo revisionMecanica.csv.")


        datos = arch.readline()

        while datos:
            datos = arch.readline().rstrip("\n")  # Lee la siguiente línea        
            
            if datos != "":
                numeroCamion, identificacion, totalTiempo, totalDistancia, totalCarga, cantidadViajes = datos.split(";")
                        
                numeroCamion = int(numeroCamion)
                identificacion = int(identificacion)
                totalTiempo = int(totalTiempo)
                totalDistancia = int(totalDistancia)
                totalCarga = int(totalCarga)
                cantidadViajes = int(cantidadViajes)
                
                distanciaArch.write(f"{numeroCamion};{totalDistancia} KM;{totalCarga} Tn;{cantidadViajes}\n")

                tiempoProm = totalTiempo / cantidadViajes
                dias = tiempoProm // 24
                horas = tiempoProm % 24
                minutos = (tiempoProm * 60) % 60

                tiempoPromedioArch.write(f"{numeroCamion};{dias}d;{horas}hr;{minutos}min\n")

                consumoDiesel = (30 / 100) * totalDistancia  # Calcula el consumo
                dieselArch.write(f"{numeroCamion};{consumoDiesel:.2f} L/100km\n")

                if totalDistancia > 20000:  # Filtra según la distancia
                    revisionMecanicaArch.write(f"{numeroCamion};{totalDistancia} KM\n")
                
        print("Se creo el archivo distancia.csv.")
        print("Se creo el archivo tiempoPromedio.csv.")
        print("Se creo el archivo consumoDiesel.csv.")
        print("Se creo el archivo revisionMecanica.csv.")
                           
    finally:
        # Cerrar todos los archivos utilizados
        arch.close()
        distanciaArch.close()
        tiempoPromedioArch.close()
        dieselArch.close()
        revisionMecanicaArch.close()


        

def main():
    camiones_data, cargas_data = ingresoDeDatos()
    '''
    lista_identificacion = []
    for c in lista_carga:
        for carga in c:
            if carga[0] not in lista_identificacion:
                lista_identificacion.append(carga[0])
    
    matriz_cargas = cargar_matriz_recursivo(lista_camiones, lista_identificacion, lista_carga)
    
    print("Matriz de Cargas:")
    'print("")
    imprimirMatriz(matriz_cargas, lista_identificacion)
    '''
    
    claves = list(cargas_data.keys())
    
    resultado = {}
    resultado = cargar_matriz_recursivo(claves, cargas_data, resultado)
    
    print("")
    print("Cantida de viajes por chofer", resultado)

    print("")
    guardarInformes()
    

if __name__ == "__main__":
    main()
