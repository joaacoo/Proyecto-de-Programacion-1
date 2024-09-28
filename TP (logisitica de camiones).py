import random

from ingresoDeCamiones import ingresoDeDatos


def cargarMatriz(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga):
    # Crear la matriz con encabezados
    matriz = [["Camion", "Tiempo", "Distancia", "Cantidad de viajes", "Carga"]]
    
    # Iterar sobre las listas para poblar la matriz
    matriz += [[camiones, tiempo, distancia, contTiempo, carga] for camiones, tiempo, distancia, contTiempo, carga in zip(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga)]
    
    return matriz

def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%20s" % str(matriz[f][c]), end=" ")  # Formato para alinear y mostrar bien los datos
        print()

# Función para imprimir los datos con formato alineado
def analisisDatos(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga):

    for i in range(len(lista_camiones)):
        # Calculamos el tiempo promedio en horas
        promedioTiempoHoras = lista_tiempo[i] / lista_contTiempo[i]
        
        # Transformamos en días y horas
        dias = str(int(promedioTiempoHoras // 24))        
        horas = str(int(promedioTiempoHoras % 24)).zfill(2)
        minutos = str(int((promedioTiempoHoras * 60) % 60)).zfill(2)
        
        # Promedio de carga transportada por viaje
        promedioCarga = lista_carga[i] / lista_contTiempo[i]
        
        # Consumo total de litros (30 litros por cada 100 km)
        consumoDiesel = (30 / 100) * lista_distancia[i]
        
        # Si algún camión recorrió en total más de 20000 km deberá ser retirado para revisión mecánica
        revisionMecanica = (" revisión mecanica.").upper() if lista_distancia[i] > 20000 else ""
                
        print(f"El camion {lista_camiones[i]} manejo un tiempo promedio de: {dias}d {horas}h {minutos}m, consumio de diesel: {consumoDiesel:.2f} L/100km y promedio de carga: {promedioCarga:.2f} Tn/Viaje.{revisionMecanica}")        
        print()

# Función principal
def main():
    # Llamamos a la función que va a devolver la lista de los datos ingresados
    lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga = ingresoDeDatos()
    matriz = cargarMatriz(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga)
    
    print("Resultados:")
    imprimirMatriz(matriz)
    
    print()
    print("Analisis de datos:")
    analisisDatos(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga) 


if __name__ == "__main__":
    main()