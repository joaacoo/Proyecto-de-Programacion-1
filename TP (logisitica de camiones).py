from ingresoDeCamiones import ingresoDeDatos, crearCSV



def cargar_matriz_recursivo(camiones, identificaciones, cargas):
    if not camiones:  # Caso base: lista vacía
        return []


    camion = camiones[0]  # Tomar el primer camión
    fila = [camion]  # Solo el número de camión


    for iden in identificaciones:
        carga = 0  # Inicializar la carga en 0
        for carga_info in cargas[0]:  # Recorre cada elemento en la primera lista de 'cargas'
            if carga_info[0] == iden:  # Solo incluye los elementos donde el primer valor es igual a 'iden'
                carga += carga_info[1]  # Suma el segundo valor a 'carga'

        fila.append(f"{carga} (Tn)" if carga > 0 else "0")

    return [fila] + cargar_matriz_recursivo(camiones[1:], identificaciones, cargas[1:])  # Llamada recursiva con el resto



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



def guardarDatos(camiones_data):
    # Archivo de la distancia recorrida
    try:
        with open("distancia.csv", mode='w') as distanciaArch:
            distanciaArch.write("Numero de Camion;Distancia Recorrida\n")
            for numeroCamion, datos in camiones_data.items():
                # Verificar que la distancia esté definida
                if 'distancia' in datos:
                    distanciaArch.write(f"{numeroCamion};{datos['distancia']} KM\n")
            print("Se almacenaron los datos de recorrido en el archivo distancia.csv.")
        
    except IOError:
        print("No se pudo crear el archivo distancia.csv.")
        
    # Archivo del tiempo promedio
    try:
        with open('tiempoPromedio.csv', mode='w') as arch:
            arch.write('Numero de Camion;Días;Horas;Minutos\n')
            for camion, data in camiones_data.items():
                total_tiempo = data['tiempo'] if 'tiempo' in data else 0  # Verificar si existe 'tiempo'
                dias = total_tiempo // 24
                horas = (total_tiempo % 24)
                minutos = (total_tiempo * 60) % 60
                
                arch.write(f"{camion};{dias}d;{horas}hr;{minutos}min\n")
            print("Se almacenaron los tiempos promedios en tiempoPromedio.csv.")
    
    except IOError:
        print("No se pudo crear el archivo tiempoPromedio.csv.")

    # Archivo de consumo de diésel
    try:
        with open("consumoDiesel.csv", mode='w') as dieselArch:
            dieselArch.write("Numero de Camion;Consumo de Diesel(L)\n")
            for numeroCamion, datos in camiones_data.items():
                if 'distancia' in datos:
                    consumoDiesel = (30 / 100) * datos['distancia']  # Calcular el consumo
                    dieselArch.write(f"{numeroCamion};{consumoDiesel:.2f} L/100km\n")
            print("Se almacenaron los datos de consumo de diésel en el archivo consumoDiesel.csv.")
        
    except IOError:
        print("No se pudo crear el archivo consumoDiesel.csv.")
        
    # Archivo de revisión mecánica
    try:
        with open("revisionMecanica.csv", mode='w') as arch:
            arch.write("Numero de Camion;Distancia Recorrida (KM)\n")
            for numeroCamion, datos in camiones_data.items():
                if 'distancia' in datos and datos['distancia'] > 20000:  # Filtrar según la distancia
                    arch.write(f"{numeroCamion};{datos['distancia']}\n")
            print("Se almacenaron los datos en el archivo revisionMecanica.csv.")
        
    except IOError:
        print("No se pudo crear el archivo revisionMecanica.csv.")

        

def main():
    lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga, camiones_data = ingresoDeDatos()
    
    lista_identificacion = []
    for c in lista_carga:
        for carga in c:
            if carga[0] not in lista_identificacion:
                lista_identificacion.append(carga[0])
    
    matriz_cargas = cargar_matriz_recursivo(lista_camiones, lista_identificacion, lista_carga)

    print("Matriz de Cargas:")
    print("")
    imprimirMatriz(matriz_cargas, lista_identificacion)
    
    print("")
    guardarDatos(camiones_data)
    

if __name__ == "__main__":
    main()
