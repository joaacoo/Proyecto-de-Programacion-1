import random 

# Declaramos la función para ingresar los datos de los camiones
def ingresoDeDatos():
    # Definimos la variable que va a retornar la función
    camiones = []
    
    # Solicitamos el ingreso de camiones
    numeroCamion = int(input("Ingrese el número de camión (-1 para terminar) "))
    
    # Solicitamos el ingreso de camiones hasta que ingrese (-1)
    while numeroCamion != -1:
        # Contamos la cantidad de veces que se ingresó el mismo camión para luego hacer el promedio de tiempo
        contTiempo = 1
        
        # Solicitamos el ingreso de tiempo        
        tiempo = int(input("Ingrese el tiempo empleado (horas) "))
        # Validamos que el tiempo ingresado sea correcto
        while tiempo <= 0:
            tiempo = int(input("El tiempo debe ser mayor a 0. Ingrese el tiempo empleado (horas) "))
            
        # Solicitamos el ingreso de la distancia
        distancia = float(input("Ingrese la distancia recorrida (km) "))
        # Validamos que la distancia ingresada sea correcta
        
        while distancia <= 0:
            distancia = float(input("La distancia debe ser mayor a 0. Ingrese la distancia recorrida (km) "))
        
        # Solicitamos el ingreso de la carga
        carga = float(input("Ingrese la carga transportada (toneladas) "))
        # Validamos que la carga ingresada sea correcta
        while carga <= 0 or carga >=32:
            carga = float(input("La carga total debe ser mayor a 0 y menor o igual a 32. Ingrese la carga transportada (toneladas) "))

        
        # Validamos que el camión no esté previamente en la lista
        posicion = -1
        
        # Recorremos la lista de camiones que hay hasta el momento para validar si el camión ya se ingresó
        largo = len(camiones)
        for i in range(largo):
            camion = camiones[i]
            if numeroCamion == camion[0]:
                # Guardamos la posición de la lista para obtener los datos
                posicion = i
        
        # Si la posición es mayor a -1, el camión está en la lista
        if posicion != -1:
            # Sumamos en cada variable de tiempo, distancia y carga los valores que venían de la lista
            tiempo = int(camiones[posicion][1]) + tiempo
            contTiempo = int(camiones[posicion][2]) + 1
            distancia = float(camiones[posicion][3]) + distancia
            carga = float(camiones[posicion][4]) + carga
            # Eliminamos el camión de la lista porque después se agrega con los datos actualizados
            camiones.pop(posicion)
                            
        # Agregamos los datos en la lista
        camiones.append([numeroCamion, tiempo, contTiempo, distancia, carga])
        
        # Solicitamos el ingreso del próximo camión
        numeroCamion = int(input("Ingrese el número de camión (-1 para terminar) "))  
    
    # Devolvemos los valores ingresados
    return camiones

# Función para imprimir los datos con formato alineado
def imprimirDatos(camiones):
    # Arrays de datos para camiones y mercancías
    camiones_marca = ["Iveco", "Mercedes", "Renault", "Scania", "Volvo"]
    mercancias = ["Maíz", "Soja", "Coca Cola", "Arroz", "Trigo", "Leche", "Carne", "Aceite", "Frutas", "Verduras", 
              "Papel", "Plástico", "Madera", "Piedra", "Cemento", "Acero", "Herramientas", "Ropa", "Electrónica", 
              "Automóviles", "Productos Químicos", "Fertilizantes", "Juguetes", "Medicamentos", "Vinos", "Cervezas", 
              "Agua Embotellada", "Pescado", "Mariscos", "Lácteos", "Pan", "Harina", "Azúcar", "Café", "Té", 
              "Chocolate", "Refrescos", "Jugos", "Sal", "Especias", "Salsas", "Conservas", "Helados", "Queso", 
              "Yogur", "Miel", "Galletas", "Pasteles", "Alimentos Congelados", "Comida Para Mascotas", "Ropa De Cama", 
              "Colchones", "Muebles", "Productos De Limpieza", "Cosméticos", "Jabones", "Champús", "Papel Higiénico", 
              "Pañales", "Toallas", "Cámaras", "Teléfonos", "Computadoras", "Tabletas", "Electrodomésticos", 
              "Bicicletas", "Motos", "Neumáticos", "Aceites Lubricantes", "Herramientas De Jardinería", "Plantas", 
              "Semillas", "Fertilizantes Orgánicos", "Maquinaria Agrícola", "Equipos De Construcción", "Juguetes Para Niños", 
              "Artículos De Papelería", "Libros", "Revistas", "Periódicos", "Juguetes Para Mascotas", "Productos Deportivos", 
              "Bicicletas De Montaña", "Equipos De Camping", "Instrumentos Musicales", "Vinilos", "Discos Compactos", 
              "Decoraciones De Hogar", "Artículos De Cocina", "Cubiertos", "Platos", "Vasos", "Ollas", "Sartenes", 
              "Productos De Ferretería", "Pinturas", "Brochas", "Rodillos", "Cadenas", "Candados", "Extintores"]
    # Usamos sort para ordenar la lista con la carga de toneladas
    camiones.sort(key=lambda x: x[4])
    
    # Encabezados con ancho fijo
    print("{:<10} {:<10} {:<20} {:<20} {:<15} {:<15} {:<20} {:<15} {:<30}".format(
        "Camion", "Marca", "Tiempo promedio", "Distancia recorrida", "Mercadería", "Carga Total", "Prom. Carga", "Consumo total","Ejes"))
    
    for camion in camiones:
        # Calculamos el tiempo promedio en horas
        promedioTiempoHoras = camion[1] / camion[2]
        
        # Transformamos en días y horas
        dias = int(promedioTiempoHoras // 24)
        horas = int(promedioTiempoHoras % 24)
        
        # Promedio de carga transportada por viaje
        promedioCarga = camion[4] / camion[2]
        
        # Consumo total de litros (30 litros por cada 100 km)
        consumoDiesel = (30 / 100) * camion[3]
        
        
        # Si algún camión recorrió en total más de 20000 km deberá ser retirado para revisión mecánica
        revisionMecanica = "Revisión" if camion[3] > 20000 else ""
        
        #Ejes del camion 
        ejes= 2
        if camion[4] >18: 
            ejes = 3
        elif camion[4] >=26:
            ejes = 4
        # Imprimimos la información de cada camión con formato alineado
        print("{:<10} {:<10} {:<20} {:<20} {:<15} {:<15} {:<20} {:<15}{:<30}".format(
            camion[0], 
            random.choice(camiones_marca),  # Seleccionamos una marca aleatoria
            f"{dias}d {horas}h", 
            f"{camion[3]:.2f} km", 
            random.choice(mercancias),  # Seleccionamos una mercadería aleatoria
            f"{camion[4]:.2f} Tn", 
            f"{promedioCarga:.2f} Tn/Viaje", 
            f"{consumoDiesel:.2f} L/100km ",
            f"{ejes} Ejes" + revisionMecanica))
        
        

# Función principal
def main():
    # Llamamos a la función que va a devolver la lista de los datos ingresados
    camiones = ingresoDeDatos() 
    imprimirDatos(camiones) 




if __name__ == "__main__":
    main()
