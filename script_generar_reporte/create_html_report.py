# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:36:26 2021

@author: fromero
"""

# Recomendaciones
# 1. Instalar python 3.6.1 https://www.python.org/downloads/release/python-361/
# 2. Instalar la librería leila -> pip install leila

# 3. Importar las librerías requeridas
import xml.etree.ElementTree as ET
import pandas as pd
import os
from leila.reporte import generar_reporte


def generate_report(xml_file):
    # 4. Leer el archivo xml
    xml_data = ET.parse(xml_file)

    # 5. Obtener el elemento raíz del árbol xml
    raiz = xml_data.getroot() 

    # 6. Obtener los nombres de columnas del archivo xml
    cols = []
    nodo_cols = raiz[0]
    for col in nodo_cols:
        cols.append(col.tag)

    # 7. Obtener los datos del archivo xml
    datos = []
    for i in range(len(raiz.getchildren())):
        child = raiz.getchildren()[i]
        datos.append([subchild.text for subchild in child.getchildren()])

    # 8. Convertir los datos a un dataframe
    df = pd.DataFrame(datos)  # Create DataFrame and transpose it

    # 9. Actualizar nombres de columnas
    df.columns = cols  # Update column names

    # 10. Convertir datos de tipo Object a numeric si corresponde
    df = df.apply(pd.to_numeric, errors='ignore')

    # 11. Generar reportes
    file_name, extesnsion  = os.path.splitext(xml_file)
    generar_reporte(df, titulo = "CALIDAD DE DATOS", archivo = file_name + ".html")


if __name__ == '__main__':
    generate_report('CCF0412-002A022020.xml')