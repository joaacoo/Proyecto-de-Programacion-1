import random

def ingresoDeDatos():
    lista_camiones = []
    camiones_data = {}
    cargas_data = {}

    numeroCamion = input("Ingrese el número del camión (-1 para terminar): ")

    while numeroCamion != "-1":
        try:
            numeroCamion = int(numeroCamion)

            if numeroCamion < 1:
                print("Ingrese un número de camión válido (-1 para terminar).")
            else:
                identificacion = input("Ingrese un número de identificación: ")

                try:
                    identificacion = int(identificacion)

                    if identificacion < 0:
                        print("Ingrese un número de identificación válido.")
                    else:
                        tiempo = random.randint(1, 35)
                        distancia = random.randint(1, 99999)
                        carga = random.randint(1, 32)

                        if numeroCamion not in camiones_data:
                            camiones_data[numeroCamion] = {
                                'tiempo': tiempo,
                                'distancia': distancia,
                                'identificacion': identificacion,
                                'contTiempo': 1
                            }
                            cargas_data[numeroCamion] = [(identificacion, carga)]
                        else:
                            camiones_data[numeroCamion]['tiempo'] += tiempo
                            camiones_data[numeroCamion]['distancia'] += distancia
                            camiones_data[numeroCamion]['contTiempo'] += 1
                            cargas_data[numeroCamion].append((identificacion, carga))

                        if numeroCamion not in lista_camiones:
                            lista_camiones.append(numeroCamion)

                except ValueError:
                    print("El valor ingresado para identificación no es válido.")

        except ValueError:
            print("El valor ingresado no es válido.")

        numeroCamion = input("Ingrese el número del camión (-1 para terminar): ")

    return camiones_data, cargas_data

def crearCSV(camiones_data, cargas_data):
    try:
        with open('camion_iden.csv', mode='w') as arch:
            arch.write('Numero de Camion;Identificacion\n')
            for camion, data in camiones_data.items():
                arch.write(f"{camion};{data['identificacion']}\n")
        print("Se han almacenado los datos en el archivo 'camion_iden.csv'")         

    except IOError:
        print("No se pudo crear el archivo") 

    try:
        with open('informes.csv', mode='w') as arch:
            arch.write('Cargas(Tn);Distancia Recorrida(KM);Tiempo empleado\n')
            for camion, cargas in cargas_data.items():
                for carga in cargas:
                    arch.write(f"{carga[1]};{camiones_data[camion]['distancia']};{camiones_data[camion]['tiempo']}\n")
        print("Se han almacenado los datos en el archivo 'informes.csv'")        

    except IOError:
        print("No se pudo crear el archivo")

# Ejecución del programa
camiones_data, cargas_data = ingresoDeDatos()
crearCSV(camiones_data, cargas_data)
