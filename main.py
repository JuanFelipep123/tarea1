from contador_archivos import ContadorArchivos

def main():
    ruta_carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra_objetivo = input("Ingrese la palabra que desea buscar: ")

    contador_archivos = ContadorArchivos(ruta_carpeta, palabra_objetivo)
    ocurrencias_archivos, total_ocurrencias = contador_archivos.contar_ocurrencias_palabra()
    if total_ocurrencias > 0:  
        contador_archivos.mostrar_resultados(ocurrencias_archivos, total_ocurrencias)

if __name__ == "__main__":
    main()
