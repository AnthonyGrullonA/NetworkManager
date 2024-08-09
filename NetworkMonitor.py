import os
import sys
import subprocess
import time
import signal
from datetime import datetime, timedelta
import requests
import msvcrt  # Importar msvcrt para manejar la entrada del teclado en Windows

# Limpiar consola
os.system("cls")

# Variables iniciales
target = "8.8.8.8"  # IP o dominio que deseas monitorear
timeout_count = 0
packet_loss_count = 0
total_pings = 0
timeout_durations = []
timeout_start = None
successful_pings = 0  # Variable para contar los pings exitosos
total_downtime_seconds = 0  # Variable para acumular tiempo sin internet


# Funcion para obtener IP publica y proveedor
def get_public_ip_info():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        return (
            data.get("ip"),
            data.get("org"),
            data.get("city"),
            data.get("region"),
            data.get("country"),
        )
    except Exception as e:
        print(f"Error al obtener informacion de IP publica: {e}")
        return None, None, None, None, None


# Funcion para generar el reporte en formato string
def generate_report():
    end_time = datetime.now()
    total_runtime_seconds = (end_time - start_time).total_seconds()

    # Cálculo de uptime en porcentaje, asegurando que no exceda el 100%
    if total_pings > 0:
        uptime_percentage = (successful_pings / total_pings) * 100
        uptime_percentage = min(uptime_percentage, 100.0)
    else:
        uptime_percentage = 0

    # Calculando el tiempo total sin internet
    total_downtime_seconds = sum(timeout_durations, timedelta()).total_seconds()

    # Informacion del Proveedor
    public_ip, org, city, region, country = get_public_ip_info()
    report = []
    report.append(
        "\n==================== Reporte de Conectividad de Red ====================\n"
    )

    report.append("\n**Informacion del Proveedor**")
    if public_ip:
        report.append(f"  Proveedor: {org}")
        report.append(f"  IP Publica: {public_ip}")
        report.append(f"  Ubicacion: {city}, {region}, {country}")
    else:
        report.append("  No se pudo obtener informacion del proveedor.")

    # Metricas de Tiempo
    report.append("\n**Metricas de Tiempo**")
    report.append(f"  Tiempo total de ejecucion: {end_time - start_time}")
    report.append(f"  Tiempo de uptime: {str(timedelta(seconds=successful_pings))}")
    report.append(
        f"  Tiempo sin internet: {str(timedelta(seconds=total_downtime_seconds))}"
    )
    report.append(
        f"  Duracion total de timeouts: {str(timedelta(seconds=total_downtime_seconds))}"
    )

    # Metricas de Conectividad
    report.append("\n**Metricas de Conectividad**")
    report.append(f"  Cantidad de pings enviados: {total_pings}")
    report.append(f"  Cantidad de pings perdidos: {packet_loss_count}")
    report.append(f"  Cantidad de pings recibidos: {successful_pings}")

    # Porcentajes de Servicio
    report.append("\n**Porcentajes de Servicio**")
    report.append(f"  Porcentaje de estabilidad del servicio: {uptime_percentage:.2f}%")

    report.append(
        "\n=======================================================================\n"
    )
    return "\n".join(report)


# Funcion para imprimir las metricas y guardar en archivo
def print_and_save_report():
    report = generate_report()
    print(report)

    public_ip, org, city, region, country = get_public_ip_info()
    if org and public_ip:
        file_name = f"{org.split()[0]}-{public_ip}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
    else:
        file_name = f"REPORT-UNKNOWN-{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"

    with open(file_name, "w") as file:
        file.write(report)

    print(f"Reporte guardado como {file_name}")


# Asignar el manejador de señal para Ctrl+C
def signal_handler(sig, frame):
    print_and_save_report()
    os._exit(0)


signal.signal(signal.SIGINT, signal_handler)

# Inicio del monitoreo
start_time = datetime.now()
print(
    "Iniciando monitoreo de red... Presiona Enter para ver metricas y guardar un reporte, o Ctrl+C para detener y generar el reporte final."
)

try:
    while True:
        # Realizar ping
        result = subprocess.run(
            ["ping", "-n", "1", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        total_pings += 1

        if b"Reply from" in result.stdout:
            successful_pings += 1
            if timeout_start:
                timeout_duration = datetime.now() - timeout_start
                timeout_durations.append(timeout_duration)
                timeout_start = None
        else:
            timeout_count += 1
            packet_loss_count += 1
            if not timeout_start:
                timeout_start = datetime.now()

        # Comprobar si se ha presionado Enter
        if msvcrt.kbhit() and msvcrt.getch() == b"\r":
            print_and_save_report()

        time.sleep(1)

except Exception as e:
    print(f"Error en el script: {e}")
    os._exit(1)
