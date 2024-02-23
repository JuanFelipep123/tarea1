import os
import re

class ContadorOcurrencias:
    def __init__(self, ruta_archivo: str, palabra_objetivo: str):
        self.ruta_archivo = ruta_archivo
        self.palabra_objetivo = palabra_objetivo

    def contar_ocurrencias_en_archivo(self) -> int:
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                ocurrencias = self.contar_ocurrencias_en_texto(contenido)
                return ocurrencias
        except FileNotFoundError:
            print(f"El archivo {self.ruta_archivo} no fue encontrado.")
            return 0
        except Exception as e:
            print(f"Error al leer el archivo {self.ruta_archivo}: {e}")
            return 0

    def contar_ocurrencias_en_texto(self, texto: str) -> int:
        ocurrencias = len(re.findall(rf'\b{re.escape(self.palabra_objetivo)}\b', texto, flags=re.IGNORECASE))
        return ocurrencias