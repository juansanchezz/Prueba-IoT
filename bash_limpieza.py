import os
import subprocess

# Función para ejecutar comandos en la terminal y obtener la salida
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

# Función para verificar el espacio en disco
def check_disk_space():
    disk_usage = run_command("df -h")
    print("Disk Usage:\n", disk_usage)

# Función para identificar archivos grandes
def find_large_files(directory, size):
    command = f"sudo find {directory} -type f -size +{size}M"
    large_files = run_command(command)
    print(f"Large files in {directory}:\n", large_files)
    return large_files.splitlines()

# Función para limpiar archivos temporales y caches
def clean_temp_and_cache():
    run_command("sudo apt-get clean")
    run_command("sudo rm -rf /tmp/*")
    run_command("sudo rm -rf /var/tmp/*")

# Función para desinstalar paquetes innecesarios
def remove_unnecessary_packages():
    run_command("sudo apt-get autoremove -y")

# Función para comprimir archivos grandes
def compress_large_files(files):
    for file in files:
        run_command(f"gzip {file}")

# Función para verificar el uso de inodos
def check_inodes():
    inodes_usage = run_command("df -i")
    print("Inodes Usage:\n", inodes_usage)

# Función principal
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
