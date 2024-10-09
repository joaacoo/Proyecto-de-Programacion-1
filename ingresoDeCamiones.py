import random

# Declaramos la función para ingresar los datos de los camiones
def ingresoDeDatos():
    lista_camiones = []
    lista_tiempo = []
    lista_contTiempo = []
    lista_distancia = []
    lista_carga = []

    # Solicitar el ingreso del primer camión
    numeroCamion = int(input("Ingrese el número del camión (-1 para terminar): "))
    
    while numeroCamion != -1:
        try:
            # Validar que el número del camión sea positivo
            if numeroCamion < 1:
                print("Ingrese un número de camión válido (-1 para terminar).")
            else:
                identificacion = int(input("Ingrese un número de identificación: "))
                
                if identificacion < 0:
                    print("Ingrese un número de identificación válido.")
                else:
                    # Solicitar y validar el tiempo, distancia y carga
                    tiempo = random.randint(1, 35)
                    distancia = random.randint(1, 99999)
                    carga = random.randint(1, 32)

                    camion_existente = False
                    
                    # Verificar si el camión ya está en la lista
                    for i in range(len(lista_camiones)):
                        if lista_camiones[i] == numeroCamion:
                            camion_existente = True
                            lista_tiempo[i] += tiempo
                            lista_distancia[i] += distancia
                            lista_contTiempo[i] += 1
                            lista_carga[i].append([identificacion, carga])  # Agregar la carga y identificación
                            break
                    
                    if not camion_existente:  # Si el camión no existe
                        lista_camiones.append(numeroCamion)
                        lista_tiempo.append(tiempo)
                        lista_distancia.append(distancia)
                        lista_contTiempo.append(1)
                        lista_carga.append([[identificacion, carga]])  # Inicializar con una lista que contenga [identificacion, carga]

        except ValueError:
            print("El valor ingresado no es válido. Asegúrese de ingresar un número entero.")
        except TypeError:
            print("Ha ocurrido un error de tipo. Verifique los datos ingresados.")
        
        # Solicitar el ingreso del próximo camión
        numeroCamion = int(input("Ingrese el número del camión (-1 para terminar): "))
    
    # Devolvemos los valores ingresados
    return lista_camiones, lista_tiempo, lista_distancia, lista_contTiempo, lista_carga
