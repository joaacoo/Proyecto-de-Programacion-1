# Gestión de Camiones

Este proyecto es una aplicación en Python para gestionar información sobre camiones, incluyendo el registro de viajes, tiempos, distancias, cargas transportadas y más. El programa también calcula el consumo de combustible y detecta camiones que necesitan revisión mecánica.

## Características

- **Ingreso de datos:** Los usuarios pueden ingresar información sobre diferentes camiones, incluyendo el número del camión, tiempo empleado, distancia recorrida y carga transportada.
- **Verificación de datos:** El sistema valida los datos de entrada para asegurar que sean correctos, como verificar que el tiempo, la distancia y la carga sean positivos y en el rango permitido.
- **Actualización de camiones:** Si un camión ya está en la lista, los datos nuevos se sumarán a los existentes.
- **Impresión de informes:** El programa genera un informe detallado que incluye:
  - Tiempo promedio empleado.
  - Distancia recorrida.
  - Carga total transportada.
  - Consumo total de diésel (30 litros por cada 100 km recorridos).
  - Camiones que superen los 20,000 km totales se marcarán para revisión mecánica.
  - Identificación del camión con mayor número de viajes.

## Requisitos

- Python 3.x

## Uso

1. **Clonar el repositorio**:
   ```bash
   git clone [https://github.com/joaacoo/Proyecto-de-Programacion-1]


## Ejecutar el script:
python main.py
## Ingreso de datos: 
El programa te pedirá ingresar datos como el número de camión, tiempo empleado (en horas), distancia recorrida (en km) y carga transportada (en toneladas).

##Reporte:
Al finalizar, el programa imprimirá una tabla con los datos de todos los camiones, indicando tiempo promedio, distancia recorrida, carga y consumo de combustible. También resaltará si algún camión necesita revisión.
## Personalización
Los nombres de las marcas de camiones y tipos de mercancías son seleccionados aleatoriamente de listas predefinidas. Puedes personalizar estas listas editando las variables camiones_marca y mercancias en el archivo main.py.
