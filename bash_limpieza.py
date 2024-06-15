import os
import subprocess

# Función para ejecutar comandos en la terminal y obtener la salida
def correr_commando(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

# Función para verificar el espacio en disco
def check_disk_space():
    disk_usage = correr_commando("df -h")
    print("uso del disco:\n", disk_usage)

# Función para identificar archivos grandes
def find_large_files(directory, size):
    command = f"sudo find {directory} -type f -size +{size}M"
    large_files = correr_commando(command)
    print(f"Archivos mas grandes en {directory}:\n", large_files)
    return large_files.splitlines()

# Función para limpiar archivos temporales y caches
def clean_temp_and_cache():
    correr_commando("sudo apt-get clean")
    correr_commando("sudo rm -rf /tmp/*")
    correr_commando("sudo rm -rf /var/tmp/*")

# Función para desinstalar paquetes innecesarios
def remove_unnecessary_packages():
    correr_commando("sudo apt-get autoremove -y")

# Función para comprimir archivos grandes
def compress_large_files(files):
    for file in files:
        correr_commando(f"gzip {file}")

# Función para verificar el uso de inodos
def check_inodes():
    inodes_usage = correr_commando("df -i")
    print("uso de los inodos:\n", inodes_usage)
def main():
    # Verificar el espacio en disco
    check_disk_space()
    
    # Identificar y comprimir archivos grandes en /var/log
    large_log_files = find_large_files("/var/log", 100)
    compress_large_files(large_log_files)

    # Limpiar archivos temporales y caches
    clean_temp_and_cache()

    # Desinstalar paquetes innecesarios
    remove_unnecessary_packages()

    # Verificar el uso de inodos
    check_inodes()
    
    # Verificar el espacio en disco nuevamente
    check_disk_space()

if __name__ == "__main__":
    main()