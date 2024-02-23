from administrador_archivos import AdministradorArchivos
from contador_ocurrencias import ContadorOcurrencias
from typing import Dict, List
import os

class ContadorArchivos:
    def __init__(self, ruta_carpeta: str, palabra_objetivo: str):
        self.ruta_carpeta = ruta_carpeta
        self.palabra_objetivo = palabra_objetivo

    def contar_ocurrencias_palabra(self) -> Dict[str, int]:
        file_manager = AdministradorArchivos(self.ruta_carpeta)
        archivos = file_manager.obtener_archivos_en_carpeta()

        if not archivos:
            print("\nNo se encontraron archivos de texto en la carpeta.")
            return {}, 0  
        
        ocurrencias_archivos = {}
        total_ocurrencias = 0

        for archivo in archivos:
            ruta_archivo = os.path.join(self.ruta_carpeta, archivo)
            contador_ocurrencias = ContadorOcurrencias(ruta_archivo, self.palabra_objetivo)
            ocurrencias = contador_ocurrencias.contar_ocurrencias_en_archivo()
            
            ocurrencias_archivos[archivo] = ocurrencias
            total_ocurrencias += ocurrencias
        
        return ocurrencias_archivos, total_ocurrencias

    def mostrar_resultados(self, ocurrencias_archivos: Dict[str, int], total_ocurrencias: int):
        print("\nResultados:")
        for archivo, ocurrencias in ocurrencias_archivos.items():
            print(f"{archivo}: {ocurrencias} ocurrencias de '{self.palabra_objetivo}'")
        print(f"\nTotal en toda la carpeta: {total_ocurrencias} ocurrencias de '{self.palabra_objetivo}'")