import random


def guardarDatosEnCsv(camiones_data, cargas_data):
    # Guardar datos de camiones en camion_iden.csv
    try:
        with open('camionIden.csv', mode='w') as arch: 
            arch.write('Numero de Camion;Identificacion del chofer;Total tiempo;Total distancia (KM);Total carga (Tn);Cantidad viajes\n')
            for numeroCamion, data in camiones_data.items():
                arch.write(f"{numeroCamion};{data['identificacion']};{data['totalTiempo']};{data['totalDistancia']};{data['totalCarga']};{data['cantidadViajes']}\n")
            
            print("Se almacenaron los datos de recorrido en el archivo camionIden.csv.")
            
            arch.close()
            
    except IOError:
        print("No se pudo guardar los datos de camiones en camionIden.csv.")
        

    # Guardar datos de cargas en informes.csv
    try:
        with open('informes.csv', mode='w') as arch: 
            arch.write('Numero de Camion;Identificacion;Cargas (Tn);Distancia Recorrida (KM);Tiempo empleado\n')
            
            for numeroCamion, cargas in cargas_data.items():
                for data in cargas:
                    arch.write(f"{numeroCamion};{data['identificacion']};{data['carga']};{data['tiempo']};{data['distancia']}\n")
            
            print("Se almacenaron los datos de recorrido en el archivo informes.csv.")
            
            arch.close()

    except IOError:
        print("No se pudo guardar los datos de informes en 'informes.csv'.")



def ingresoDeDatos():
    camiones_data = {}  # Diccionario para almacenar los datos de cada camión
    cargas_data = {}    # Diccionario para almacenar cada viaje que hizo el camión
    
    # Solicitar el ingreso del primer camión
    numeroCamion = input("Ingrese el número del camión (-1 para terminar): ")
    
    while numeroCamion != "-1":
        try:
            numeroCamion = int(numeroCamion)

            # Validar que el número del camión sea positivo
            if numeroCamion < 1:
                print("Ingrese un número de camión válido (-1 para terminar).")
            else:
                identificacion = input("Ingrese un número de identificación del chofer: ")
                
                try:
                    identificacion = int(identificacion)

                    if identificacion < 1:
                        print("Ingrese un número de identificación válido.")
                    else:
                        # Solicitar y validar el tiempo, distancia y carga
                        tiempo = random.randint(1, 35)
                        distancia = random.randint(1, 99999)
                        carga = random.randint(1, 32)

                        # Agregar o actualizar datos del camión
                        if numeroCamion not in camiones_data:
                            camiones_data[numeroCamion] = {
                                'identificacion': identificacion,
                                'totalTiempo': tiempo,
                                'totalDistancia': distancia,                                
                                'totalCarga': carga,
                                'cantidadViajes': 1,
                            }
                            #inicializo la lista para las cargas de este camion en particular
                            cargas_data[numeroCamion] = []
                        else:
                            camiones_data[numeroCamion]['totalTiempo'] += tiempo
                            camiones_data[numeroCamion]['totalDistancia'] += distancia
                            camiones_data[numeroCamion]['totalCarga'] += carga
                            camiones_data[numeroCamion]['cantidadViajes'] += 1
                        
                        cargas_data[numeroCamion].append({
                                'identificacion': identificacion,
                                'carga': carga,
                                'tiempo': tiempo,                                
                                'distancia': distancia})
                        
                except ValueError:
                    print("El valor ingresado para identificación no es válido.")

        except ValueError:
            print("El valor ingresado no es válido.")

        # Solicitar el ingreso del próximo camión
        numeroCamion = input("Ingrese el número del camión (-1 para terminar): ")
    
    print("")
    
    guardarDatosEnCsv(camiones_data, cargas_data)

    return camiones_data, cargas_data
        