import numpy as np

def obtener_datos_sii():

    archivo = "data/dolar_observado_sii_2022_2025.csv"

    datos_crudos = np.genfromtxt(archivo, delimiter=',', skip_header=1, dtype=str)

    anios = datos_crudos[:, 0].astype(int)
    nombres_meses = datos_crudos[:, 1] 
    meses_num = datos_crudos[:, 2].astype(int)
    precios = datos_crudos[:, 3].astype(float)

    '''Lo que hace esto es tomar las columnas del archivo y las convierte en filas; Ademas esta forma nos permite 
    extrer los datos de forma vectorizada'''
    
    return anios, nombres_meses, precios
