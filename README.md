# Proyecto de Monitoreo de Conectividad de Red

## Descripción del Proyecto

Este proyecto proporciona un script en Python diseñado para monitorear la conectividad de red mediante la ejecución de pings a un objetivo específico (dirección IP o dominio) y generar un informe sobre el estado de la conexión. El script registra los tiempos de inactividad, la estabilidad de la red, y muestra información sobre la IP pública y el proveedor de servicios de internet (ISP).

## Funcionalidades

1. **Monitoreo Continuo**: El script realiza pings a un objetivo designado en intervalos de 1 segundo y registra el número de pings exitosos y fallidos.
2. **Registro de Tiempo de Inactividad**: El script calcula el tiempo total de inactividad de la red basado en la duración de los pings fallidos.
3. **Obtención de Información Pública de IP**: Utiliza el servicio `ipinfo.io` para obtener información sobre la IP pública y el ISP.
4. **Interfaz de Usuario Simple**: Permite al usuario presionar Enter en cualquier momento para ver las métricas actuales, o usar Ctrl+C para generar un reporte final y detener el script.
5. **Reporte de Conectividad**: Al finalizar, el script genera un reporte que incluye el tiempo total de ejecución, tiempo de uptime, tiempo de inactividad, cantidad de pings enviados, pings perdidos, y porcentaje de estabilidad del servicio.

## Requisitos

### Requerimientos del Sistema

- **Sistema Operativo**: Windows (El script utiliza el comando `cls` para limpiar la pantalla y el comando `ping` con la opción `-n`, específicos de Windows).
- **Python**: Versión 3.6 o superior.
- **Conexión a Internet**: Necesaria para obtener la información de la IP pública.

### Dependencias de Python

Las siguientes bibliotecas de Python son necesarias para ejecutar el script:

- `requests`: Para realizar solicitudes HTTP a `ipinfo.io`.
- `subprocess`: Para ejecutar comandos de ping en la línea de comandos.
- `datetime`: Para manejar y calcular tiempos.
- `os`: Para ejecutar comandos en el sistema operativo.
- `threading`: Para manejar la captura de entrada de usuario en un hilo separado.
- `signal`: Para manejar señales como Ctrl+C.

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install requests
```

# Ejecución del Script

## Clonar el Repositorio

Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/AnthonyGrullonA/NetworkManager.git
cd monitor-red
```

1.  Clona el repositorio en tu máquina local.
2.  Navega al directorio del proyecto.

## Ejecutar el Script

Para ejecutar el script, sigue estos pasos:

```bash
python NetworkMonitor.py
```

1. Ejecuta el script.
2. Una vez iniciado, el script comenzará a monitorear la conectividad de red hacia la IP o dominio configurado.

## Interacción del Usuario

- **Presionar Enter**: Muestra las métricas actuales del monitoreo sin detener el script.
- **Presionar Ctrl+C**: Detiene el script y genera un reporte final con todas las métricas recopiladas.

## Archivo

- Luego de acada Interacción de enter crea un documento TXT con la info del reporte.

## Ejemplo de Salida

```bash
Iniciando monitoreo de red... Presiona Enter para ver métricas, o Ctrl+C para detener y generar el reporte final.

==================== Reporte de Conectividad de Red ====================

**Información del Proveedor**
  Proveedor: Google LLC
  IP Pública: 8.8.8.8
  Ubicación: Mountain View, California, United States

**Métricas de Tiempo**
  Tiempo total de ejecución: 0:05:00
  Tiempo de uptime: 0:04:50
  Tiempo sin internet: 0:00:10
  Duración total de timeouts: 0:00:10

**Métricas de Conectividad**
  Cantidad de pings enviados: 300
  Cantidad de pings perdidos: 10
  Cantidad de pings recibidos: 290

**Porcentajes de Servicio**
  Porcentaje de estabilidad del servicio: 96.67%

=======================================================================
```
