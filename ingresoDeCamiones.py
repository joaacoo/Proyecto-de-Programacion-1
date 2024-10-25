import random


def crearCSV():

    try:
        with open('camionIden.csv', mode='w') as arch:
            arch.write('Numero de Camion;Identificacion\n')
        print("Se han almacenado los datos en el archivo 'camionIden.csv")         

    except IOError:
        print("No se pudo crear el archivo") 

    try:
        with open('informes.csv', mode='w') as arch:
            arch.write('Cargas(Tn);Distancia Recorrida(KM);Tiempo empleado\n')
        print("Se han almacenado los datos en el archivo 'informes.csv")        

    except IOError:
        print("No se pudo crear el archivo")

    return 'informes.csv', 'camionIden.csv'


def ingresoDeDatos():
    lista_camiones = []
    camiones_data = {}  # Diccionario para almacenar los datos de cada camión
    cargas_data = {}    # Diccionario para almacenar las cargas de cada camión

    # Solicitar el ingreso del primer camión
    numeroCamion = input("Ingrese el número del camión (-1 para terminar): ")
    
    while numeroCamion != "-1":
        try:
            numeroCamion = int(numeroCamion)

            # Validar que el número del camión sea positivo
            if numeroCamion < 1:
                print("Ingrese un número de camión válido (-1 para terminar).")
            else:
                identificacion = input("Ingrese un número de identificación: ")
                
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
                                'tiempo': tiempo,
                                'distancia': distancia,
                                'identificacion': identificacion,
                                'contTiempo': 1
                            }
                            cargas_data[numeroCamion] = [(identificacion, carga)]  # Inicializar carga
                        else:
                            camiones_data[numeroCamion]['tiempo'] += tiempo
                            camiones_data[numeroCamion]['distancia'] += distancia
                            camiones_data[numeroCamion]['contTiempo'] += 1
                            cargas_data[numeroCamion].append((identificacion, carga))  # Agregar carga

                        if numeroCamion not in lista_camiones:
                            lista_camiones.append(numeroCamion)

                except ValueError:
                    print("El valor ingresado para identificación no es válido.")

        except ValueError:
            print("El valor ingresado no es válido.")

        # Solicitar el ingreso del próximo camión
        numeroCamion = input("Ingrese el número del camión (-1 para terminar): ")
    
    # Devolvemos los valores ingresados
    lista_tiempo = [camiones_data[camion]['tiempo'] for camion in lista_camiones]
    lista_distancia = [camiones_data[camion]['distancia'] for camion in lista_camiones]
    lista_contTiempo = [camiones_data[camion]['contTiempo'] for camion in lista_camiones]
    lista_carga = [cargas_data[camion] for camion in lista_camiones]
        
    return lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga, camiones_data


def guardarDatosEntrada(camiones_data, cargas_data):
    # Guardar datos de camiones en camion_iden.csv
    try:
        with open('camionIden.csv', mode='w') as arch:  # Cambiado a 'w' para sobrescribir
            for numeroCamion, data in camiones_data.items():
                arch.write(f"{numeroCamion};{data['identificacion']}\n")
                print("Se almacenaron los datos de recorrido en el archivo camionIden.csv.")
    except IOError:
        print("No se pudo guardar los datos de camiones en camionIden.csv.")

    # Guardar datos de cargas en informes.csv
    try:
        with open('informes.csv', mode='w') as arch:  # Cambiado a 'w' para sobrescribir
            for numeroCamion, cargas in cargas_data.items():
                for identificacion, carga in cargas:
                    tiempo = camiones_data[numeroCamion]['tiempo']
                    distancia = camiones_data[numeroCamion]['distancia']
                    arch.write(f"{carga};{distancia};{tiempo}\n")  # Aquí se pone '0' como ejemplo para consumo de diesel
                    print("Se almacenaron los datos de recorrido en el archivo camionIden.csv.")

    except IOError:
        print("No se pudo guardar los datos de informes en 'informes.csv'.")
        
