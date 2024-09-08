import random

from ingresoDeCamiones import ingresoDeDatos


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
    print("{:<10} {:<10} {:<20} {:<20} {:<15} {:<15} {:<20} {:<15}".format(
        "Camion", "Marca", "Tiempo promedio", "Distancia recorrida", "Mercadería", "Carga Total", "Prom. Carga", "Consumo total"))
    
    maxViajes = 0

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
        
    
        # Imprimimos la información de cada camión con formato alineado
        print("{:<10} {:<10} {:<20} {:<20} {:<15} {:<15} {:<20} {:<15}".format(
            camion[0], 
            random.choice(camiones_marca),  # Seleccionamos una marca aleatoria
            f"{dias}d {horas}h", 
            f"{camion[3]:.2f} km", 
            random.choice(mercancias),  # Seleccionamos una mercadería aleatoria
            f"{camion[4]:.2f} Tn", 
            f"{promedioCarga:.2f} Tn/Viaje", 
            f"{consumoDiesel:.2f} L/100km" + revisionMecanica))      
        

# Función principal
def main():
    # Llamamos a la función que va a devolver la lista de los datos ingresados
    camiones = ingresoDeDatos() 
    imprimirDatos(camiones) 


if __name__ == "__main__":
    main()