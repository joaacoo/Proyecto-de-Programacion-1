from ingresoDeCamiones import ingresoDeDatos
import csv

def cargar_matriz(camiones, identificaciones, cargas):
    # Crear la matriz con encabezados
    matriz = [["Numero Camion", "Identificacion", "Carga (Tn)"]]
    
    # Crear filas para cada combinación de camión e identificación
    for i in range(len(camiones)):
        camion = camiones[i]
        for carga_info in cargas[i]:
            identificacion = carga_info[0]
            carga = carga_info[1]
            fila = [camion, identificacion, f"{carga} (Tn)"]
            matriz.append(fila)
    
    return matriz

def imprimirMatriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(f"{str(elemento):>20}", end=" ")  # Alinear a la derecha
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
                
        print(f"El camion {lista_camiones[i]} manejó un tiempo promedio de: {dias}d {horas}h {minutos}m, distancia recorrida: {lista_distancia[i]} KM, consumió diesel: {consumoDiesel:.2f} L/100km y promedio de carga: {promedioCarga:.2f} Tn/Viaje.{revisionMecanica}")        
        print()
    
    camiones_mas_distancia = [lista_camiones[i] for i in range(len(lista_distancia)) if lista_distancia[i] > 0]
    distancias = [lista_distancia[i] for i in range(len(lista_distancia)) if lista_distancia[i] > 0]
         
    if len(camiones_mas_distancia) == 1:  # Si solo hay un camión en la lista
        print("Camiones que recorrieron más distancia (sin el que menos recorrió):")
        print(camiones_mas_distancia)  # Imprimir el único camión
    elif distancias:
        min_distancia = distancias[0]
        indice_min_distancia = 0
        
        for i in range(1, len(distancias)):
            if distancias[i] < min_distancia:
                min_distancia = distancias[i]
                indice_min_distancia = i
        
        camiones_filtrados = camiones_mas_distancia[:indice_min_distancia] + camiones_mas_distancia[indice_min_distancia+1:]
        
        print("Camiones que recorrieron más distancia (sin el que menos recorrió):")
        print(camiones_filtrados)
    else:
        print("No hay camiones con distancia registrada.")

def guardar_en_csv(matriz, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for fila in matriz:
            writer.writerow(fila)
    print(f"Datos guardados en {nombre_archivo}")

def main():
    lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga = ingresoDeDatos()
    
    # Obtenemos todas las identificaciones únicas (opcional, ya no es necesario para esta estructura)
    
    matriz_cargas = cargar_matriz(lista_camiones, None, lista_carga)
    
    print("Matriz de Cargas:")
    print("")
    imprimirMatriz(matriz_cargas)
    
    print()
    print("Análisis de datos:")
    analisisDatos(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga)
    
    guardar_en_csv(matriz_cargas, "matriz_cargas.csv")

if __name__ == "__main__":
    main()
