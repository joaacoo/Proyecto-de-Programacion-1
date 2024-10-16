
from ingresoDeCamiones import ingresoDeDatos
import csv


def cargar_matriz(camiones, identificaciones, cargas):
    # Crear la matriz con encabezados
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
            fila.append(f"{carga} (Tn)" if carga > 0 else "0")  # Agregar carga a la fila
        matriz.append(fila)

    return matriz

def imprimirMatriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(f"{str(elemento):>20}", end=" ")  # Alinear a la derecha
        print()

def analisisDatos(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga):
    for i in range(len(lista_camiones)):
        promedioTiempoHoras = lista_tiempo[i] / lista_contTiempo[i]
        
        dias = str(int(promedioTiempoHoras // 24))        
        horas = str(int(promedioTiempoHoras % 24)).zfill(2)
        minutos = str(int((promedioTiempoHoras * 60) % 60)).zfill(2)
        
        carga_total = sum(c[1] for c in lista_carga[i])

        promedioCarga = carga_total / lista_contTiempo[i] if lista_contTiempo[i] > 0 else 0
        
        consumoDiesel = (30 / 100) * lista_distancia[i]
        
        revisionMecanica = (" revisión mecánica.").upper() if lista_distancia[i] > 20000 else ""
                
        print(f"El camión {lista_camiones[i]} manejó un tiempo promedio de: {dias}d {horas}h {minutos}m, "
              f"distancia recorrida: {lista_distancia[i]} KM, consumió diesel: {consumoDiesel:.2f} L/100km "
              f"y promedio de carga: {promedioCarga:.2f} Tn/Viaje.{revisionMecanica}")        
        print()
    
    camiones_mas_distancia = [lista_camiones[i] for i in range(len(lista_distancia)) if lista_distancia[i] > 0]
    distancias = [lista_distancia[i] for i in range(len(lista_distancia)) if lista_distancia[i] > 0]
         
    if len(camiones_mas_distancia) == 1:  # Si solo hay un camión en la lista
        print("Camiones que recorrieron más distancia (sin el que menos recorrió):")
        print(camiones_mas_distancia)  # Imprimir el único camión
    elif distancias:
        min_distancia = min(distancias)
        indice_min_distancia = distancias.index(min_distancia)
        
        camiones_filtrados = camiones_mas_distancia[:indice_min_distancia] + camiones_mas_distancia[indice_min_distancia + 1:]
        
        print("Camiones que recorrieron más distancia (sin el que menos recorrió):")
        print(camiones_filtrados)
    else:
        print("No hay camiones con distancia registrada.")

def guardar_en_csv(matriz, nombre_archivo):
    # Transponer la matriz para convertir filas en columnas
    matriz_transpuesta = zip(*matriz)

    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        for columna in matriz_transpuesta:
            writer.writerow(columna)
    
    print(f"Datos guardados en columnas en {nombre_archivo}")

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
    
    print(f"{'Identificación':>40}", end=" ")  # Alinear la palabra "Identificación"
    print()
    imprimirMatriz(matriz_cargas)
    
    print()
    print("Análisis de datos:")
    analisisDatos(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga)
    
    guardar_en_csv(matriz_cargas, "matriz_cargas.csv")

if __name__ == "__main__":
    main()
