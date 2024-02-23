import os
from typing import Dict, List

class AdministradorArchivos:
    def __init__(self, ruta_carpeta: str):
        self.ruta_carpeta = ruta_carpeta

    def obtener_archivos_en_carpeta(self) -> List[str]:
        try:
            files = [archivo for archivo in os.listdir(self.ruta_carpeta) if archivo.endswith(('.txt', '.xml', '.json', '.csv'))]
            return files
        except FileNotFoundError:
            print(f"\nLa carpeta {self.ruta_carpeta} no fue encontrada.")
            return []