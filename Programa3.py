import csv  # Importa el módulo para leer y escribir archivos CSV
import json  # Importa el módulo para leer archivos JSON (Punto 4)
import os  # Importa el módulo para interactuar con el sistema operativo
import xml.etree.ElementTree as ET  # Importa el módulo para leer archivos XML (Punto 4)

# Bucle principal para mantener el menú activo
while True:
    print("\n===== MENÚ DE OPCIONES =====")
    print("1. Listar archivos de la carpeta (Nombre, extensión y ruta)")
    print("2. Leer el contenido completo del archivo Usuarios.csv")
    print(
        "3. Imprimir columnas específicas (Nombres, Apellidos, Dependencia, Estado, Cantidad columnas) de Usuarios.csv"
    )
    print(
        "4. Procesar lineamientos para archivos Programación.xml y Servicios.json"
    )
    print("5. Salir del programa")
    print("-" * 40)

    opcion = input("Selecciona una opción (1-5): ")

    # ==========================================
    # PUNTO 1: Listar archivos de la carpeta
    # ==========================================
    if opcion == "1":
        print("\n" + "=" * 40)
        print("PUNTO 1: LISTA DE ARCHIVOS EN LA CARPETA")
        print("=" * 40)
        ruta = "."  # Carpeta actual
        archivos_encontrados = False

        for archivo in os.listdir(ruta):
            if os.path.isfile(archivo):
                archivos_encontrados = True
                nombre, extension = os.path.splitext(archivo)
                print(f"Nombre: {nombre}")
                print(f"Extension: {extension}")
                print(f"Ruta: {os.path.abspath(archivo)}")
                print("-" * 40)

        if not archivos_encontrados:
            print("No se encontraron archivos en esta carpeta.")

    # ==========================================
    # PUNTO 2: Leer el contenido completo del CSV
    # ==========================================
    elif opcion == "2":
        print("\n" + "=" * 40)
        print("PUNTO 2: CONTENIDO COMPLETO DE USUARIOS.CSV")
        print("=" * 40)
        try:
            with open("Usuarios.csv", "r", encoding="utf-8") as archivo_csv:
                lector = csv.reader(archivo_csv, delimiter=";")
                for fila in lector:
                    print(
                        fila
                    )  # Muestra la línea completa (como lista) del archivo original
            print("-" * 40)
        except FileNotFoundError:
            print("Error: El archivo 'Usuarios.csv' no existe en esta carpeta.")

    # ==========================================
    # PUNTO 3: Imprimir columnas específicas del CSV
    # ==========================================
    elif opcion == "3":
        print("\n" + "=" * 40)
        print("PUNTO 3: COLUMNAS ESPECÍFICAS DE USUARIOS.CSV")
        print("=" * 40)
        try:
            with open("Usuarios.csv", "r", encoding="utf-8") as archivo_csv:
                lector = csv.DictReader(archivo_csv, delimiter=";")
                for usuario in lector:
                    print(f"Nombres: {usuario.get('Nombres', 'N/A')}")
                    print(f"Apellidos: {usuario.get('Apellidos', 'N/A')}")
                    print(f"Dependencia: {usuario.get('Dependencia', 'N/A')}")
                    print(f"Estado: {usuario.get('Estado', 'N/A')}")
                    print(f"Cantidad de columnas: {len(usuario)}")
                    print("-" * 40)
        except FileNotFoundError:
            print("Error: El archivo 'Usuarios.csv' no existe en esta carpeta.")

    # ==========================================
    # PUNTO 4: Lineamientos XML y JSON
    # ==========================================
    elif opcion == "4":
        print("\n" + "=" * 40)
        print("PUNTO 4: LINEAMIENTOS XML Y JSON")
        print("=" * 40)

        # Sub-proceso para Servicios.json
        print("--- Leyendo Servicios.json ---")
        try:
            with open("Servicios.json", "r", encoding="utf-8") as archivo_json:
                datos_json = json.load(archivo_json)
                print(
                    json.dumps(datos_json, indent=4, ensure_ascii=False)
                )  # Lo imprime formateado bonito
        except FileNotFoundError:
            print("Aviso: El archivo 'Servicios.json' no fue encontrado.")
        except json.JSONDecodeError:
            print("Error: 'Servicios.json' no tiene un formato JSON válido.")

        print("-" * 40)

        # Sub-proceso para programacion.xml
        print("--- Leyendo programacion.xml ---")
        try:
            arbol = ET.parse("programacion.xml")
            raiz = arbol.getroot()
            print(f"Elemento raíz del XML: {raiz.tag}")
            # Recorre e imprime la estructura básica del XML
            for hijo in raiz:
                print(f"  Elemento: {hijo.tag} | Atributos: {hijo.attrib}")
                for sub_hijo in hijo:
                    print(f"    {sub_hijo.tag}: {sub_hijo.text}")
        except FileNotFoundError:
            print("Aviso: El archivo 'programacion.xml' no fue encontrado.")
        except ET.ParseError:
            print("Error: 'programacion.xml' no tiene un formato XML válido.")
        print("-" * 40)

    # ==========================================
    # SALIR
    # ==========================================
    elif opcion == "5":
        print("Saliendo del programa... ¡Adiós!")
        break

    else:
        print("Opción inválida. Por favor, selecciona un número entre 1 y 5.")
