from ingresoDeCamiones import ingresoDeDatos


def cargar_matriz_recursivo(camiones, identificaciones, cargas):
    if not camiones:  # Caso base: lista vacía
        return []

    camion = camiones[0]  # Tomar el primer camión
    fila = [camion]  # Solo el número de camión

    for iden in identificaciones:
        carga = sum(carga_info[1] for carga_info in cargas[0] if carga_info[0] == iden)
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


def analisisDatosRecursivo(camiones, tiempos, distancias, contTiempos, cargas):
    if not camiones:  # Caso base: lista vacía
        return

    camion = camiones[0]
    promedioTiempoHoras = tiempos[0] / contTiempos[0]
    
    dias = str(int(promedioTiempoHoras // 24))
    horas = str(int(promedioTiempoHoras % 24)).zfill(2)
    minutos = str(int((promedioTiempoHoras * 60) % 60)).zfill(2)
    
    carga_total = sum(c[1] for c in cargas[0])
    promedioCarga = carga_total / contTiempos[0] if contTiempos[0] > 0 else 0
    consumoDiesel = (30 / 100) * distancias[0]
    revisionMecanica = (" revisión mecánica.").upper() if distancias[0] > 20000 else ""

    print()
    print(f"El camión {camion} manejó un tiempo promedio de: {dias}d {horas}h {minutos}m, "
          f"distancia recorrida: {distancias[0]} KM, consumió diesel: {consumoDiesel:.2f} L/100km "
          f"y promedio de carga: {promedioCarga:.2f} Tn/Viaje.{revisionMecanica}")

    # Llama recursivamente con el resto de las listas
    analisisDatosRecursivo(camiones[1:], tiempos[1:], distancias[1:], contTiempos[1:], cargas[1:])


def guardarDatos(camiones_data):
    acumulador_kilometros = {}

    # Acumular kilómetros por número de camión
    for numeroCamion, datos in camiones_data.items():
        if datos['distancia'] > 20000:
            if numeroCamion not in acumulador_kilometros:
                acumulador_kilometros[numeroCamion] = {
                    'identificacion': datos['identificacion'],
                    'distancia': datos['distancia']
                }
            else:
                acumulador_kilometros[numeroCamion]['distancia'] += datos['distancia']

    try:
        with open("revisionMecanica.txt", mode='w') as arch:
            for numeroCamion, datos in acumulador_kilometros.items():
                # Escribir en el formato especificado
                arch.write(f"Número de camión: {numeroCamion}; Identificación: {datos['identificacion']}; Distancia recorrida: {datos['distancia']}\n")
        print("Se han almacenado los datos en el archivo 'revisionMecanica.txt'.")
    except IOError:
        print("No se pudo crear el archivo.")


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
    print("Análisis de datos:")
    analisisDatosRecursivo(lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga)
    
    print("")
    guardarDatos(camiones_data)


if __name__ == "__main__":
    main()