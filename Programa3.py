import os  # Importa el módulo para interactuar con el sistema operativo
import csv  # Importa el módulo para leer y escribir archivos CSV

print("===== LISTA DE ARCHIVOS =====")  # Imprime un encabezado en la consola

ruta = "."  # Define la variable ruta como el directorio actual

# Inicia un bucle para recorrer cada elemento dentro de la ruta especificada
for archivo in os.listdir(ruta):
    # Verifica si el elemento actual es un archivo y no una carpeta
    if os.path.isfile(archivo):
        # Separa el nombre del archivo de su extensión (ej: 'Usuarios' y '.csv')
        nombre, extension = os.path.splitext(archivo)

        print(f"Nombre: {nombre}")  # Imprime el nombre del archivo
        print(f"Extension: {extension}")  # Imprime la extensión del archivo
        # Imprime la ruta completa y absoluta del archivo en el sistema
        print(f"Ruta: {os.path.abspath(archivo)}")
        print("-" * 40)  # Imprime una línea divisoria de 40 guiones

print("\n===== DATOS DEL CSV =====")  # Imprime encabezado con un salto de línea previo

# Abre el archivo CSV en modo lectura ('r') y con codificación UTF-8 para tildes y eñes
with open("Usuarios.csv", "r", encoding="utf-8") as archivo_csv:
    # Lee el CSV mapeando cada fila como un diccionario usando ';' como separador
    lector = csv.DictReader(archivo_csv, delimiter=";")

    # Inicia un bucle para recorrer fila por fila los usuarios del archivo
    for usuario in lector:
        print(f"Nombres: {usuario['Nombres']}")  # Imprime el valor de la columna 'Nombres'
        print(f"Apellidos: {usuario['Apellidos']}")  # Imprime el valor de la columna 'Apellidos'
        print(f"Dependencia: {usuario['Dependencia']}")  # Imprime la columna 'Dependencia'
        print(f"Estado: {usuario['Estado']}")  # Imprime la columna 'Estado'

        total_columnas = len(usuario)  # Cuenta el número de columnas (campos) en la fila actual
        print(f"Cantidad de columnas: {total_columnas}")  # Imprime el total de columnas

        print("-" * 40)  # Imprime una línea divisoria para el siguiente registro
