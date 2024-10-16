from ingresoDeCamiones import ingresoDeDatos
import csv

def cargar_matriz(camiones, identificaciones, cargas):
    # Crear la matriz con encabezados (puedes incluir las unidades aquí si lo deseas)
    matriz = [["Numero Camiones"] + identificaciones]

    # Crear filas para cada camión
    for camion in camiones:
        fila = [camion]  # Comenzar la fila con el número del camión
        for iden in identificaciones:
            carga = 0  # Inicializar carga en 0
            # Verificar si hay carga para el camión y la identificación
            for i in range(len(cargas)):
                if camiones[i] == camion:  # Coincidencia de camión
                    for carga_info in cargas[i]:
                        if carga_info[0] == iden:  # Coincidencia de identificación
                            carga += carga_info[1]  # Sumar carga
            fila.append(carga)  # Agregar carga numérica a la fila sin unidades
        matriz.append(fila)

    return matriz

def imprimirMatriz(matriz):
    # Asumiendo que deseas imprimir las unidades al mostrar la matriz
    # Añadimos las unidades solo para imprimir, no en los datos de la matriz
    encabezados = matriz[0]
    print(f"{'':>20}", end=" ")  # Espacio para el primer encabezado
    for encabezado in encabezados[1:]:
        print(f"{str(encabezado):>20}", end=" ")
    print()
    for fila in matriz[1:]:
        print(f"{str(fila[0]):>20}", end=" ")  # Imprimir número de camión
        for elemento in fila[1:]:
            print(f"{str(elemento) + ' (Tn)':>20}", end=" ")  # Añadir unidades al imprimir
        print()

def analisisDatos(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga):
    for i in range(len(lista_camiones)):
        promedioTiempoHoras = lista_tiempo[i] / lista_contTiempo[i] if lista_contTiempo[i] > 0 else 0
        
        dias = str(int(promedioTiempoHoras // 24))        
        horas = str(int(promedioTiempoHoras % 24)).zfill(2)
        minutos = str(int((promedioTiempoHoras * 60) % 60)).zfill(2)
        
        carga_total = 0
        for c in lista_carga[i]:
            carga_total += c[1]

        promedioCarga = carga_total / lista_contTiempo[i] if lista_contTiempo[i] > 0 else 0
        
        consumoDiesel = (30 / 100) * lista_distancia[i]
        
        revisionMecanica = (" REVISION MECANICA.").upper() if lista_distancia[i] > 20000 else ""
                
        print(f"El camión {lista_camiones[i]} manejó un tiempo promedio de: {dias}d {horas}h {minutos}m, distancia recorrida: {lista_distancia[i]} KM, consumió diesel: {consumoDiesel:.2f} L/100km y promedio de carga: {promedioCarga:.2f} Tn/Viaje.{revisionMecanica}")        
        print()
    
    camiones_mas_distancia = [lista_camiones[i] for i in range(len(lista_distancia)) if lista_distancia[i] > 0]
    distancias = [lista_distancia[i] for i in range(len(lista_distancia)) if lista_distancia[i] > 0]
         
    if len(camiones_mas_distancia) == 1:  # Si solo hay un camión en la lista
        print("Camiones que recorrieron más distancia (sin el que menos recorrió):")
        print(camiones_mas_distancia)  # Imprimir el único camión
    elif distancias:
        min_distancia = min(distancias)
        indice_min_distancia = distancias.index(min_distancia)
        
        camiones_filtrados = camiones_mas_distancia[:indice_min_distancia] + camiones_mas_distancia[indice_min_distancia+1:]
        
        print("Camiones que recorrieron más distancia (sin el que menos recorrió):")
        print(camiones_filtrados)
    else:
        print("No hay camiones con distancia registrada.")

def guardar_en_csv(matriz, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        for fila in matriz:
            writer.writerow(fila)
    print(f"Datos guardados en {nombre_archivo}")

def main():
    lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga = ingresoDeDatos()
    
    lista_identificacion = []
    for c in lista_carga:
        for carga in c:
            if carga[0] not in lista_identificacion:  # Comprobar que la identificación no está en la lista
                lista_identificacion.append(carga[0])
    
    matriz_cargas = cargar_matriz(lista_camiones, lista_identificacion, lista_carga)
    
    print("Matriz de Cargas:")
    print("")
    imprimirMatriz(matriz_cargas)
    
    print()
    print("Análisis de datos:")
    analisisDatos(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga)
    
    guardar_en_csv(matriz_cargas, "matriz_cargas.csv")

if __name__ == "__main__":
    main()
